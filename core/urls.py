from django.urls import include, path
from .views import about_view, search_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('search/', search_view, name='search'),
]
