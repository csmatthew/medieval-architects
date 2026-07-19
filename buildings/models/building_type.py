from django.db import models
from django.core.exceptions import ValidationError

CATEGORY_CHOICES = [
    ("ecclesiastical", "Ecclesiastical"),
    ("domestic", "Domestic"),
    ("military", "Military"),
    ("civic", "Civic / Urban"),
]

SUBTYPE_CHOICES = [
    # Ecclesiastical
    ("abbey", "Abbey"),
    ("priory", "Priory"),
    ("friary", "Friary"),
    ("cathedral", "Cathedral"),
    ("collegiate_church", "Collegiate Church"),
    ("parish_church", "Parish Church"),
    # Domestic
    ("manor_house", "Manor House"),
    ("hall_house", "Hall House"),
    ("farmstead", "Farmstead"),
    # Military
    ("castle", "Castle"),
    ("tower_house", "Tower House"),
    ("fortified_manor", "Fortified Manor"),
    # Civic
    ("guildhall", "Guildhall"),
    ("market_hall", "Market Hall"),
    ("gatehouse", "Gatehouse"),
    ("memorial_cross", "Memorial Cross"),
]


class BuildingType(models.Model):
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        help_text="Broad category of building type",
    )

    subtype = models.CharField(
        max_length=20,
        choices=SUBTYPE_CHOICES,
        help_text="Specific type of building",
    )

    name = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    @classmethod
    def grouped_choices(cls):
        groups = {}
        for obj in cls.objects.all().order_by("category", "subtype"):
            groups.setdefault(obj.category, []).append((obj.id, obj.name))

        return [(category, choices) for category, choices in groups.items()]

    def clean(self):
        mapping = {
            "ecclesiastical": {
                "abbey",
                "priory",
                "friary",
                "cathedral",
                "collegiate_church",
                "parish_church",
            },
            "domestic": {
                "manor_house",
                "hall_house",
                "farmstead",
            },
            "military": {
                "castle",
                "tower_house",
                "fortified_manor",
            },
            "civic": {
                "guildhall",
                "market_hall",
                "gatehouse",
                "memorial_cross",
            },
        }

        if self.subtype not in mapping[self.category]:
            raise ValidationError(
                f"{self.subtype} "
                f"is not a valid subtype for category {self.category}."
            )

    def __str__(self):
        return self.name
