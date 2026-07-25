from django.urls import path
from .views import person_detail_view

from .views import export_to_excel

urlpatterns = [
    path('export/', export_to_excel, name='people-export-excel'),
    path('<slug:slug>/', person_detail_view, name='person_detail'),
]
