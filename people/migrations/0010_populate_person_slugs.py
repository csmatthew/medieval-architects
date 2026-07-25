from django.db import migrations
from django.utils.text import slugify


def generate_unique_slug(apps, schema_editor):
    Person = apps.get_model('people', 'Person')
    existing = set()

    for person in Person.objects.all():
        # Rebuild full_name manually (properties do NOT exist in migrations)
        parts = []

        if person.given_name:
            parts.append(person.given_name)

        if person.preposition:
            parts.append(person.preposition)

        if person.surname:
            parts.append(person.surname)

        if person.label:
            parts.append(person.label)

        if person.sequence_label:
            parts.append(person.sequence_label)

        full_name = " ".join(parts)

        # Fallback if empty
        base = slugify(full_name) or f"person-{person.pk}"
        slug = base
        counter = 1

        # Ensure uniqueness (your original logic preserved)
        while slug in existing or Person.objects.filter(slug=slug).exclude(pk=person.pk).exists():
            slug = f"{base}-{counter}"
            counter += 1

        person.slug = slug
        person.save(update_fields=['slug'])
        existing.add(slug)


def noop_reverse(apps, schema_editor):
    # Do not attempt to delete slugs on reverse migration
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_person_slug'),
    ]

    operations = [
        migrations.RunPython(generate_unique_slug, noop_reverse),
    ]
