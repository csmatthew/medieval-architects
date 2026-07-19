from django.db import models
from .building_type import BuildingType


class Building(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    building_type = models.ForeignKey(
        BuildingType, on_delete=models.CASCADE, null=True, blank=True
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
