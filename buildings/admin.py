from django.contrib import admin
from django import forms
from .models.building_name import Building
from .models.building_phase import BuildingPhase
from .models.building_type import BuildingType
from .models.building_category import Category
from .models.building_subtype import Subtype
from .models.building_element import Element
from .models.georef import GeoRef
from chronology.models import UncertainDate


class GeoRefInline(admin.StackedInline):
    model = GeoRef
    extra = 0


class BuildingPhaseInline(admin.TabularInline):
    model = BuildingPhase
    extra = 0
    autocomplete_fields = ("person", "elements")


class BuildingAdminForm(forms.ModelForm):
    construction_start_year = forms.IntegerField(
        label="Year", required=False
    )
    construction_start_month = forms.IntegerField(
        label="Month", required=False, min_value=1, max_value=12
    )
    construction_start_day = forms.IntegerField(
        label="Day", required=False, min_value=1, max_value=31
    )
    construction_start_qualifier = forms.ChoiceField(
        label="Qualifier",
        choices=UncertainDate.QUALIFIERS,
        required=False,
    )
    construction_end_year = forms.IntegerField(
        label="Year", required=False
    )
    construction_end_month = forms.IntegerField(
        label="Month", required=False, min_value=1, max_value=12
    )
    construction_end_day = forms.IntegerField(
        label="Day", required=False, min_value=1, max_value=31
    )
    construction_end_qualifier = forms.ChoiceField(
        label="Qualifier",
        choices=UncertainDate.QUALIFIERS,
        required=False,
    )

    class Meta:
        model = Building
        exclude = ("construction_start", "construction_end")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_date_initial("construction_start", self.instance.construction_start)
        self._set_date_initial("construction_end", self.instance.construction_end)

    def _set_date_initial(self, prefix, uncertain_date):
        if uncertain_date is None:
            self.fields[f"{prefix}_qualifier"].initial = "exact"
            return

        self.initial.update(
            {
                f"{prefix}_year": uncertain_date.year,
                f"{prefix}_month": uncertain_date.month,
                f"{prefix}_day": uncertain_date.day,
                f"{prefix}_qualifier": uncertain_date.qualifier,
            }
        )

    def save(self, commit=True):
        building = super().save(commit=False)
        if commit:
            building.save()
        self._save_date(building, "construction_start")
        self._save_date(building, "construction_end")
        if commit:
            self.save_m2m()
        return building

    def _save_date(self, building, prefix):
        values = {
            "year": self.cleaned_data[f"{prefix}_year"],
            "month": self.cleaned_data[f"{prefix}_month"],
            "day": self.cleaned_data[f"{prefix}_day"],
            "qualifier": self.cleaned_data[f"{prefix}_qualifier"] or "exact",
        }
        current = getattr(building, prefix)
        has_values = (
            values["year"] is not None
            or values["month"] is not None
            or values["day"] is not None
            or values["qualifier"] != "exact"
        )

        if not has_values:
            if current is not None:
                setattr(building, prefix, None)
                building.save(update_fields=[prefix])
            return

        if current is None:
            current = UncertainDate.objects.create(**values)
            setattr(building, prefix, current)
            building.save(update_fields=[prefix])
            return

        for field, value in values.items():
            setattr(current, field, value)
        current.save()


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    form = BuildingAdminForm
    exclude = ("people",)
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "slug",
                "location",
                "county",
                "building_type",
            )
        }),
        ("Construction start", {
            "fields": (
                (
                    "construction_start_year",
                    "construction_start_month",
                    "construction_start_day",
                    "construction_start_qualifier",
                ),
            )
        }),
        ("Construction end", {
            "fields": (
                (
                    "construction_end_year",
                    "construction_end_month",
                    "construction_end_day",
                    "construction_end_qualifier",
                ),
            )
        }),
    )
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
