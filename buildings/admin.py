from django.contrib import admin
from .models.building_name import Building
from .models.georef import GeoRef


class GeoRefInline(admin.StackedInline):
    model = GeoRef
    extra = 0


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "county",
        "created_at",
    )
    search_fields = (
        "name",
        "location",
        "county",
    )
    filter_horizontal = ("people",)
    inlines = [GeoRefInline]
