from django.test import TestCase

from chronology.models import UncertainDate
from people.models import Person

from .admin import BuildingAdminForm
from .models.building_name import Building
from .models.building_element import Element
from .models.building_phase import BuildingPhase


class BuildingPhaseTests(TestCase):
    def test_phase_can_link_building_and_person(self):
        building = Building.objects.create(name="Test Building")
        person = Person.objects.create(given_name="Alice", surname="Mason")
        element = Element.objects.create(name="Vaulting")
        start = UncertainDate.objects.create(year=1200)
        end = UncertainDate.objects.create(year=1205)

        phase = BuildingPhase.objects.create(
            building=building,
            person=person,
            start=start,
            end=end,
            notes="First phase",
        )
        phase.elements.add(element)

        self.assertEqual(phase.building, building)
        self.assertEqual(phase.person, person)
        self.assertEqual(phase.start.display(), "1200")
        self.assertEqual(phase.end.display(), "1205")
        self.assertEqual(
            list(phase.elements.values_list("name", flat=True)),
            ["Vaulting"],
        )

    def test_building_admin_form_edits_construction_dates_inline(self):
        form = BuildingAdminForm(
            data={
                "name": "Test Building",
                "construction_start_year": "1200",
                "construction_start_month": "6",
                "construction_start_day": "15",
                "construction_start_qualifier": "circa",
                "construction_end_year": "1250",
                "construction_end_month": "",
                "construction_end_day": "",
                "construction_end_qualifier": "exact",
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        building = form.save()
        self.assertEqual(building.construction_start.display(), "1200-06-15")
        self.assertEqual(building.construction_start.qualifier, "circa")
        self.assertEqual(building.construction_end.display(), "1250")

        form = BuildingAdminForm(
            instance=building,
            data={
                "name": "Test Building",
                "construction_start_year": "",
                "construction_start_month": "",
                "construction_start_day": "",
                "construction_start_qualifier": "exact",
                "construction_end_year": "",
                "construction_end_month": "",
                "construction_end_day": "",
                "construction_end_qualifier": "exact",
            },
        )

        self.assertTrue(form.is_valid(), form.errors)
        form.save()
        building.refresh_from_db()
        self.assertIsNone(building.construction_start)
        self.assertIsNone(building.construction_end)
