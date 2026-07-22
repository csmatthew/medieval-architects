from django.contrib import admin
from .models.building_name import Building
from .models.building_phase import BuildingPhase
from .models.building_type import BuildingType
from .models.building_category import Category
from .models.building_subtype import Subtype
from .models.building_element import Element
from .models.georef import GeoRef


class GeoRefInline(admin.StackedInline):
    model = GeoRef
    extra = 0


class BuildingPhaseInline(admin.TabularInline):
    model = BuildingPhase
    extra = 0
    autocomplete_fields = ("person", "elements")


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    exclude = ("people",)
    list_display = (
        "name",
        "location",
        "county",
        "construction_start_display",
        "construction_end_display",
        "created_at",
        "building_type",
    )
    search_fields = (
        "name",
        "location",
        "county",
    )
    inlines = [GeoRefInline, BuildingPhaseInline]

    @admin.display(description="Construction Start")
    def construction_start_display(self, obj):
        if not obj.construction_start:
            return "-"

        return obj.construction_start.display()

    @admin.display(description="Construction End")
    def construction_end_display(self, obj):
        if not obj.construction_end:
            return "-"

        return obj.construction_end.display()


@admin.register(BuildingPhase)
class BuildingPhaseAdmin(admin.ModelAdmin):
    list_display = (
        "building",
        "person",
        "start_display",
        "end_display",
        "elements_display",
        "notes",
    )
    search_fields = (
        "building__name",
        "person__given_name",
        "person__surname",
        "elements__name",
        "notes",
    )
    autocomplete_fields = ("building", "person", "elements")

    @admin.display(description="Start")
    def start_display(self, obj):
        if not obj.start:
            return "-"

        return obj.start.display()

    @admin.display(description="End")
    def end_display(self, obj):
        if not obj.end:
            return "-"

        return obj.end.display()

    @admin.display(description="Elements")
    def elements_display(self, obj):
        names = list(obj.elements.values_list("name", flat=True))
        return ", ".join(names) if names else "-"


@admin.register(BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    exclude = ("elements",)
    list_display = ("category", "subtype")
    search_fields = ("category__name", "subtype__name")


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
