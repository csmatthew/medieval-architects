from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from buildings.models import Building

from .models import Person


class PersonAdminForm(forms.ModelForm):
    buildings = forms.ModelMultipleChoiceField(
        queryset=Building.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Buildings", is_stacked=False),
        help_text="Buildings associated with this person",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["buildings"].initial = self.instance.buildings.all()

    class Meta:
        model = Person
        fields = (
            "surname",
            "given_name",
            "preposition",
            "label",
            "sequence_label",
            "role",
            "floruit_start",
            "floruit_end",
            "death",
            "buildings",
        )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
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

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.instance.buildings.set(form.cleaned_data.get("buildings", []))

    @admin.display(description="Floruit Start")
    def floruit_start_display(self, obj):
        return obj.floruit_start.display() if obj.floruit_start else "-"

    @admin.display(description="Floruit End")
    def floruit_end_display(self, obj):
        return obj.floruit_end.display() if obj.floruit_end else "-"

    @admin.display(description="Death")
    def death_display(self, obj):
        return obj.death.display() if obj.death else "-"
