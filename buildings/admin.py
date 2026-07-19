from django.contrib import admin
from .models.building_name import Building
from .models.building_type import BuildingType
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
        "building_type",
    )
    search_fields = (
        "name",
        "location",
        "county",
    )
    filter_horizontal = ("people",)
    inlines = [GeoRefInline]


@admin.register(BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "subtype")
    # readonly_fields = ("name", "category", "subtype", "description")

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True
