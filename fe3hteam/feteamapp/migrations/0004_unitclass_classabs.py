# Generated by Django 4.1.5 on 2023-01-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0003_unitclass_description_unitclass_genderlocked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitclass',
            name='classAbs',
            field=models.ManyToManyField(to='feteamapp.ability'),
        ),
    ]
