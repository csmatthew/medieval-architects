from django.contrib import admin
from .models import BuildingPhase
from chronology.models import UncertainDate


class StartDateInline(admin.StackedInline):
    model = UncertainDate
    fk_name = "building_phase_start_of"
    extra = 0
    verbose_name = "Start Date"
    verbose_name_plural = "Start Date"


class EndDateInline(admin.StackedInline):
    model = UncertainDate
    fk_name = "building_phase_end_of"
    extra = 0
    verbose_name = "End Date"
    verbose_name_plural = "End Date"


@admin.register(BuildingPhase)
class BuildingPhaseAdmin(admin.ModelAdmin):
    inlines = [StartDateInline, EndDateInline]
    list_display = ("building", "person", "start", "end", "notes")
