from django.test import TestCase

from chronology.models import UncertainDate
from people.models import Person

from .models.building_name import Building
from .models.building_phase import BuildingPhase


class BuildingPhaseTests(TestCase):
    def test_phase_can_link_building_and_person(self):
        building = Building.objects.create(name="Test Building")
        person = Person.objects.create(given_name="Alice", surname="Mason")
        start = UncertainDate.objects.create(year=1200)
        end = UncertainDate.objects.create(year=1205)

        phase = BuildingPhase.objects.create(
            building=building,
            person=person,
            start=start,
            end=end,
            notes="First phase",
        )

        self.assertEqual(phase.building, building)
        self.assertEqual(phase.person, person)
        self.assertEqual(phase.start.display(), "1200")
        self.assertEqual(phase.end.display(), "1205")
