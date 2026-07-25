from django.urls import path
from .views import about_view, search_view, record_list, record_detail


urlpatterns = [
    path('about/', about_view, name='about'),
    path('search/', search_view, name='search'),
    path('record/', record_list, name='record_list'),
    path('record/<int:pk>/', record_detail, name='record_detail'),
]
