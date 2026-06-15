from django.contrib import admin
from .models import UncertainDate


@admin.register(UncertainDate)
class UncertainDateAdmin(admin.ModelAdmin):
    list_display = ("display", "qualifier", "start_year", "end_year")
    list_filter = ("qualifier",)
