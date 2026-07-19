from django.db import models


class GeoRef(models.Model):
    building = models.OneToOneField(
        "Building", on_delete=models.CASCADE, related_name="geo_ref"
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    class Meta:
        verbose_name = "Geographic Reference"
        verbose_name_plural = "Geographic References"
