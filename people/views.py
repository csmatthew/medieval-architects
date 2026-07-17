import pandas as pd
from datetime import datetime

from django.http import HttpResponse
from django.utils import timezone

from .models import Person


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
