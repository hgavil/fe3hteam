# Generated by Django 4.1.5 on 2023-01-27 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0017_remove_unit_exclusiveabilities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proficiency',
            name='level',
            field=models.CharField(blank=True, choices=[('e', 'E'), ('e+', 'E+'), ('d', 'D'), ('d+', 'D+'), ('c', 'C'), ('c+', 'C+'), ('b', 'B'), ('b+', 'B+'), ('a', 'A'), ('a+', 'A+'), ('s', 'S'), ('s+', 'S+'), ('mastery', 'Mastery'), ('bud', 'Budding Talent')], max_length=20, null=True),
        ),
    ]
