# Generated by Django 4.1.5 on 2023-01-12 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0005_ability_description_ability_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='exclusiveAbilities',
            field=models.ManyToManyField(limit_choices_to={'type': 'character'}, related_name='charex', to='feteamapp.ability'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='personalAbility',
            field=models.ForeignKey(limit_choices_to={'type': 'personal'}, on_delete=django.db.models.deletion.CASCADE, to='feteamapp.ability'),
        ),
    ]
