from django.db import models


class UncertainDate(models.Model):
    QUALIFIERS = [
        ("exact", "Exact"),
        ("circa", "Circa"),
        ("before", "Before"),
        ("after", "After"),
        ("range", "Range"),
        ("floruit", "Floruit"),
        ("unknown", "Unknown"),
    ]

    # Numeric boundaries
    start_year = models.IntegerField(null=True, blank=True)
    start_month = models.IntegerField(null=True, blank=True)
    start_day = models.IntegerField(null=True, blank=True)

    end_year = models.IntegerField(null=True, blank=True)
    end_month = models.IntegerField(null=True, blank=True)
    end_day = models.IntegerField(null=True, blank=True)

    qualifier = models.CharField(
        max_length=20, choices=QUALIFIERS, default="unknown"
    )

    class Meta:
        verbose_name = "date"
        verbose_name_plural = "dates"

    def __str__(self):
        return self.display()

    def display(self):
        # Human-friendly output
        if self.qualifier == "exact":
            if self.start_day and self.start_month:
                return f"{self.start_day}/{self.start_month}/{self.start_year}"
            return str(self.start_year)

        if self.qualifier == "circa":
            return f"c. {self.start_year}"

        if self.qualifier == "before":
            return f"before {self.end_year}"

        if self.qualifier == "after":
            return f"after {self.start_year}"

        if self.qualifier == "range":
            return f"{self.start_year}–{self.end_year}"

        if self.qualifier == "floruit":
            return f"fl. {self.start_year}–{self.end_year}"

        return "unknown"
