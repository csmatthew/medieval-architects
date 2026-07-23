from django.contrib import admin
from django.urls import path, include
from core.views import about_view
from mapper.views import mapper_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', mapper_view, name='mapper'),
    path('buildings/', include('buildings.urls')),
    path('core/', include('core.urls')),
    path('about/', about_view, name='about'),
    path('people/', include('people.urls')),
]
