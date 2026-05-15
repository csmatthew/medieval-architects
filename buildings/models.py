from django.db import models
from people.models import Person


class Building(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)

    people = models.ManyToManyField(
        Person,
        related_name="buildings",
        blank=True,
        help_text="People associated with this building"
    )

    def __str__(self):
        return self.name
