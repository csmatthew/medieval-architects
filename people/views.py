from collections import OrderedDict

from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch
import pandas as pd
from datetime import datetime

from buildings.models.building_phase import BuildingPhase
from .models import Person


def person_detail_view(request, slug):
    person = get_object_or_404(
        Person.objects.prefetch_related(
            Prefetch(
                "building_phases",
                queryset=BuildingPhase.objects.select_related(
                    "building",
                    "building__geo_ref",
                    "start",
                    "end",
                ),
            )
        ),
        slug=slug,
    )

    buildings_by_slug = OrderedDict()

    for phase in person.building_phases.all():
        geo_ref = getattr(phase.building, "geo_ref", None)
        if (
            not geo_ref
            or geo_ref.latitude is None
            or geo_ref.longitude is None
        ):
            continue

        building_entry = buildings_by_slug.setdefault(
            phase.building.slug,
            {
                "name": phase.building.name,
                "slug": phase.building.slug,
                "location": phase.building.location,
                "county": phase.building.county,
                "latitude": float(geo_ref.latitude),
                "longitude": float(geo_ref.longitude),
                "phases": [],
            },
        )

        phase_label = []
        if phase.start:
            phase_label.append(str(phase.start))
        if phase.end:
            phase_label.append(str(phase.end))
        if phase.notes:
            phase_label.append(phase.notes)

        if phase_label:
            building_entry["phases"].append(" - ".join(phase_label))

    return render(
        request,
        'people/person_detail.html',
        {
            'person': person,
            'associated_buildings_map': list(buildings_by_slug.values()),
        },
    )


def export_to_excel(request):
    data = Person.objects.all().values()
    dataframe = pd.DataFrame(list(data))

    for column in dataframe.columns:
        dataframe[column] = dataframe[column].apply(
            lambda value: (
                timezone.make_naive(value)
                if isinstance(value, datetime) and timezone.is_aware(value)
                else value
            )
        )

    response = HttpResponse(
        content_type=(
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    )
    response['Content-Disposition'] = 'attachment; filename=export.xlsx'

    dataframe.to_excel(response, index=False, engine='openpyxl')
    return response
