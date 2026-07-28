from django.urls import path
from .views import building_georef_data, building_detail_view

urlpatterns = [
    path('georef/', building_georef_data, name='building-georef-data'),
    path('<slug:slug>/', building_detail_view, name='building_detail')
]
