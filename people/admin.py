from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "surname",
        "given_name",
        "label",
        "sequence_label",
        "role",
        "created_at",
    )
    search_fields = ("surname", "given_name", "label", "role_choices")
    date_hierarchy = "created_at"
    list_filter = ("role",)
