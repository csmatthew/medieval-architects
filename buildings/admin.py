from django.contrib import admin
from .models.building_name import Building
from .models.building_type import BuildingType
from .models.building_category import Category
from .models.building_subtype import Subtype
from .models.building_element import Element
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
    list_display = ("category", "subtype")
    search_fields = ("category__name", "subtype__name", "elements__name")
    filter_horizontal = ("elements",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Subtype)
class SubtypeAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name", "category__name")


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
