from django.db import models


class Craftsperson(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        db_index=True,
    )
    forename = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    preposition = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    label = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sequence_label = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    def __str__(self):
        parts = [
            self.forename,
            self.preposition,
            self.name,
            self.label,
            self.sequence_label,
        ]
        joined = " ".join(p for p in parts if p)
        return joined or self.label or "Unnamed Craftsperson"


class Building(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    craftspeople = models.ManyToManyField(
        Craftsperson,
        related_name="buildings",
    )

    def __str__(self):
        return self.name
