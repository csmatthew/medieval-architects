from django.db import models


class BuildingType(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    subtype = models.ForeignKey("Subtype", on_delete=models.CASCADE)
    elements = models.ManyToManyField("Element", blank=True)

    def __str__(self):
        return f"{self.category} – {self.subtype}"
