from django.contrib import admin
from .models import Building


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "county",
    )
    search_fields = (
        "name",
        "location",
        "county",
    )
    filter_horizontal = ("people",)
