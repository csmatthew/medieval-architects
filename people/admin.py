from django import forms
from django.contrib import admin
from django.utils.html import format_html, format_html_join

from buildings.models.building_phase import BuildingPhase

from .models import Person


class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            "surname",
            "given_name",
            "preposition",
            "label",
            "sequence_label",
            "role",
            "floruit_start",
            "floruit_end",
            "death",
        )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    readonly_fields = ("worked_buildings_display",)
    list_display = (
        "full_name",
        "floruit_start_display",
        "floruit_end_display",
        "death_display",
        "created_at",
    )
    search_fields = ("surname", "given_name", "label", "role")
    date_hierarchy = "created_at"
    list_filter = ("role",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "surname",
                    "given_name",
                    "preposition",
                    "label",
                    "sequence_label",
                    "role",
                    "floruit_start",
                    "floruit_end",
                    "death",
                )
            },
        ),
        (
            "Buildings Worked On",
            {
                "fields": ("worked_buildings_display",),
            },
        ),
    )

    @admin.display(description="Buildings")
    def buildings_display(self, obj):
        buildings = (
            BuildingPhase.objects.filter(person=obj)
            .select_related("building")
            .values_list("building__name", flat=True)
            .distinct()
        )
        buildings = list(buildings)
        return ", ".join(buildings) if buildings else "-"

    @admin.display(description="Buildings Worked On")
    def worked_buildings_display(self, obj):
        phases = (
            BuildingPhase.objects.filter(person=obj)
            .select_related("building")
            .prefetch_related("elements")
            .order_by("building__name", "id")
        )

        grouped_buildings = {}
        for phase in phases:
            building = phase.building
            building_entry = grouped_buildings.setdefault(
                building.id,
                {
                    "name": building.name,
                    "elements": [],
                },
            )
            for element in phase.elements.all():
                element_name = element.name
                if element_name not in building_entry["elements"]:
                    building_entry["elements"].append(element_name)

        if not grouped_buildings:
            return "-"

        items = []
        for building in grouped_buildings.values():
            if building["elements"]:
                items.append(
                    (
                        building["name"],
                        ", ".join(building["elements"]),
                    )
                )
            else:
                items.append((building["name"], ""))

        return format_html(
            "<ul style='margin:0; padding-left:1.2em;'>{}</ul>",
            format_html_join(
                "",
                "<li>{}{}{}</li>",
                (
                    (
                        name,
                        " - " if elements else "",
                        elements,
                    )
                    for name, elements in items
                ),
            ),
        )

    @admin.display(description="Floruit Start")
    def floruit_start_display(self, obj):
        return obj.floruit_start.display() if obj.floruit_start else "-"

    @admin.display(description="Floruit End")
    def floruit_end_display(self, obj):
        return obj.floruit_end.display() if obj.floruit_end else "-"

    @admin.display(description="Death")
    def death_display(self, obj):
        return obj.death.display() if obj.death else "-"
