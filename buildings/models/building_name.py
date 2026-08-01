from django.db import models
from django.utils.text import slugify
from chronology.models import UncertainDate
from .building_type import BuildingType


class Building(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    building_type = models.ForeignKey(
        BuildingType, on_delete=models.CASCADE, null=True, blank=True
    )

    construction_start = models.OneToOneField(
        UncertainDate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="construction_start_of",
    )

    construction_end = models.OneToOneField(
        UncertainDate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="construction_end_of",
    )

    people = models.ManyToManyField(
        "people.Person",
        related_name="buildings",
        blank=True,
        help_text="People associated with this building",
    )

    county_choices = [
        ("Bedfordshire", "Bedfordshire"),
        ("Berkshire", "Berkshire"),
        ("Buckinghamshire", "Buckinghamshire"),
        ("Cambridgeshire", "Cambridgeshire"),
        ("Cheshire", "Cheshire"),
        ("Cornwall", "Cornwall"),
        ("Cumberland", "Cumberland"),
        ("Derbyshire", "Derbyshire"),
        ("Devon", "Devon"),
        ("Dorset", "Dorset"),
        ("Durham", "Durham"),
        ("Essex", "Essex"),
        ("Gloucestershire", "Gloucestershire"),
        ("Hampshire", "Hampshire"),
        ("Herefordshire", "Herefordshire"),
        ("Hertfordshire", "Hertfordshire"),
        ("Huntingdonshire", "Huntingdonshire"),
        ("Kent", "Kent"),
        ("Lancashire", "Lancashire"),
        ("Leicestershire", "Leicestershire"),
        ("Lincolnshire", "Lincolnshire"),
        ("Middlesex", "Middlesex"),
        ("Norfolk", "Norfolk"),
        ("Northamptonshire", "Northamptonshire"),
        ("Northumberland", "Northumberland"),
        ("Nottinghamshire", "Nottinghamshire"),
        ("Oxfordshire", "Oxfordshire"),
        ("Rutland", "Rutland"),
        ("Shropshire", "Shropshire"),
        ("Somerset", "Somerset"),
        ("Staffordshire", "Staffordshire"),
        ("Suffolk", "Suffolk"),
        ("Surrey", "Surrey"),
        ("Sussex", "Sussex"),
        ("Warwickshire", "Warwickshire"),
        ("Westmorland", "Westmorland"),
        ("Wiltshire", "Wiltshire"),
        ("Worcestershire", "Worcestershire"),
        ("Yorkshire", "Yorkshire"),
    ]
    """https://en.wikipedia.org/wiki/Historic_counties_of_England"""

    county = models.CharField(
        max_length=20,
        choices=county_choices,
        blank=True,
        null=True,
        help_text="Historic county in England",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name) or f"building-{self.pk or ''}"
            slug = base
            counter = 1

            while (
                type(self)
                .objects
                .filter(slug=slug)
                .exclude(pk=self.pk)
                .exists()
            ):
                slug = f"{base}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/buildings/{self.slug}/"
