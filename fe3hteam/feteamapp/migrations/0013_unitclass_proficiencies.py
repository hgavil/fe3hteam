# Generated by Django 4.1.5 on 2023-01-13 19:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0012_unitclass_uniqueto'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitclass',
            name='proficiencies',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), blank=True, size=None), blank=True, null=True, size=None),
        ),
    ]
