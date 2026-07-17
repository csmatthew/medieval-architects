from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "floruit_start_display",
        "floruit_end_display",
        "death_display",
        "created_at",
    )
    search_fields = ("surname", "given_name", "label", "role")
    date_hierarchy = "created_at"
    list_filter = ("role",)

    @admin.display(description="Floruit Start")
    def floruit_start_display(self, obj):
        return obj.floruit_start.display() if obj.floruit_start else "-"

    @admin.display(description="Floruit End")
    def floruit_end_display(self, obj):
        return obj.floruit_end.display() if obj.floruit_end else "-"

    @admin.display(description="Death")
    def death_display(self, obj):
        return obj.death.display() if obj.death else "-"
