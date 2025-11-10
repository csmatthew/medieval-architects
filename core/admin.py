from django.contrib import admin
from .models import Craftsperson, Building


@admin.register(Craftsperson)
class CraftspersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "forename",
        "preposition",
        "label",
        "sequence_label",
    )
    search_fields = ("name",)
    list_filter = ("sequence_label",)
    ordering = ("name",)


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_horizontal = ("craftspeople",)
