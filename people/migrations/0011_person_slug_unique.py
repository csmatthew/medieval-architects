from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_populate_person_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, blank=True),
        ),
    ]
