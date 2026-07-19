from django.urls import path

from .views import building_georef_data

urlpatterns = [
    path('georef/', building_georef_data, name='building-georef-data'),
]