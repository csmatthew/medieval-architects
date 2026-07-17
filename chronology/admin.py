from django import forms
from django.contrib import admin

from .models import UncertainDate


class UncertainDateAdminForm(forms.ModelForm):
    class Meta:
        model = UncertainDate
        fields = ("year", "qualifier")
        labels = {
            "year": "Date",
        }


@admin.register(UncertainDate)
class UncertainDateAdmin(admin.ModelAdmin):
    form = UncertainDateAdminForm
    list_display = ("display", "qualifier", "year")
    list_filter = ("qualifier",)
