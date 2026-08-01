from django.urls import path
from .views import (
    about_view,
    search_view,
    record_list,
    record_detail,
    record_detail_by_pk,
)


urlpatterns = [
    path('about/', about_view, name='about'),
    path('search/', search_view, name='search'),
    path('record/', record_list, name='record_list'),
    path('record/<int:pk>/', record_detail_by_pk, name='record_detail_pk'),
    path('record/<slug:slug>/', record_detail, name='record_detail'),
]
