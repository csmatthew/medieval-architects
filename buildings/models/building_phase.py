from django.db import models

from chronology.models import UncertainDate


class BuildingPhase(models.Model):
    building = models.ForeignKey(
        "Building",
        on_delete=models.CASCADE,
        related_name="phases",
    )
    person = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
        related_name="building_phases",
    )
    start = models.OneToOneField(
        UncertainDate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="building_phase_start_of",
    )
    end = models.OneToOneField(
        UncertainDate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="building_phase_end_of",
    )
    elements = models.ManyToManyField(
        "Element",
        blank=True,
        related_name="building_phases",
    )
    notes = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Building Phase"
        verbose_name_plural = "Building Phases"
        ordering = ["building", "start", "id"]

    def __str__(self):
        person_name = str(self.person)
        building_name = str(self.building)
        return f"{building_name} - {person_name}"
