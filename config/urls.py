from django.contrib import admin
from django.urls import path, include
from mapper.views import mapper_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', mapper_view, name='mapper'),
    path('buildings/', include('buildings.urls')),
    path('', include('core.urls')),
    path('people/', include('people.urls')),
]
