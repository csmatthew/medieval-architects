from django.urls import path

from .views import export_to_excel

urlpatterns = [
    path('export/', export_to_excel, name='people-export-excel'),
]
