from django.db import migrations, models
from django.utils.text import slugify


def populate_building_slugs(apps, schema_editor):
    Building = apps.get_model('buildings', 'Building')
    existing = set()

    for building in Building.objects.all().order_by('pk'):
        base = slugify(building.name) or f"building-{building.pk}"
        slug = base
        counter = 1

        while slug in existing or Building.objects.filter(slug=slug).exclude(pk=building.pk).exists():
            slug = f"{base}-{counter}"
            counter += 1

        building.slug = slug
        building.save(update_fields=['slug'])
        existing.add(slug)


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0006_buildingphase_elements'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.RunPython(populate_building_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='building',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]