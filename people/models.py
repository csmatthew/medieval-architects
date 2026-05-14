from django.db import models


class Person(models.Model):
    surname = models.CharField(max_length=100, blank=True, null=True)
    given_name = models.CharField(max_length=100, blank=True, null=True)
    preposition = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="e.g. de, von, van, ap, fitz"
    )
    label = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="e.g. the Mason, the Elder, the Younger"
    )
    sequence_label = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="e.g. II, III, Junior"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]   # oldest → newest

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """
        Builds a readable name like:
        'Nicholas de Ailington the Mason II'
        """
        parts = []

        if self.given_name:
            parts.append(self.given_name)

        if self.preposition:
            parts.append(self.preposition)

        if self.surname:
            parts.append(self.surname)

        if self.label:
            parts.append(self.label)

        if self.sequence_label:
            parts.append(self.sequence_label)

        return " ".join(parts)
