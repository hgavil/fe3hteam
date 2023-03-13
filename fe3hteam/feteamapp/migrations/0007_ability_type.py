# Generated by Django 4.1.5 on 2023-01-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0006_alter_unit_exclusiveabilities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='type',
            field=models.CharField(blank=True, choices=[('personal', 'Personal'), ('class', 'Class'), ('standard', 'Standard'), ('character', 'Character Exclusive')], max_length=50, verbose_name='Type'),
        ),
    ]