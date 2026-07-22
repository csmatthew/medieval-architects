from datetime import date

from django.db import models


class UncertainDate(models.Model):
    QUALIFIERS = [
        ("exact", "Exact"),
        ("circa", "Circa"),
        ("before", "Before"),
        ("after", "After"),
        ("range", "Range"),
        ("unknown", "Unknown"),
    ]

    # Numeric boundaries
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)

    qualifier = models.CharField(
        max_length=20, choices=QUALIFIERS, default="exact"
    )

    class Meta:
        verbose_name = "date"
        verbose_name_plural = "dates"

    def __str__(self):
        return self.display()

    def display(self):
        # Human-friendly output
        if self.year is None:
            return "unknown"

        if self.month is not None and self.day is not None:
            try:
                return date(self.year, self.month, self.day).isoformat()
            except ValueError:
                pass

        if self.qualifier == "exact":
            return str(self.year)

        if self.qualifier == "circa":
            return f"c. {self.year}"

        if self.qualifier == "before":
            return f"before {self.year}"

        if self.qualifier == "after":
            return f"after {self.year}"

        return str(self.year)
