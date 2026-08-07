from django.contrib import admin
from django.urls import path, include
from mapper.views import mapper_view
from core.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name='home'),
    path('map/', mapper_view, name='mapper'),
    path('buildings/', include('buildings.urls')),
    path('', include('core.urls')),
    path('people/', include('people.urls')),
]
