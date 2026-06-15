from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "birth_display",
        "floruit_display",
        "death_display",
        "created_at",
    )
    search_fields = ("surname", "given_name", "label", "role_choices")
    date_hierarchy = "created_at"
    list_filter = ("role",)

    @admin.display(description="Birth")
    def birth_display(self, obj):
        return obj.birth.display() if obj.birth else ""

    @admin.display(description="Floruit")
    def floruit_display(self, obj):
        return obj.floruit.display() if obj.floruit else ""

    @admin.display(description="Death")
    def death_display(self, obj):
        return obj.death.display() if obj.death else ""
