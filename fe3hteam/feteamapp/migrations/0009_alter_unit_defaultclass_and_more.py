# Generated by Django 4.1.5 on 2023-01-12 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0008_alter_unit_defaultclass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='defaultClass',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='feteamapp.unitclass'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='exclusiveAbilities',
            field=models.ManyToManyField(blank=True, default='', limit_choices_to={'type': 'character'}, related_name='charex', to='feteamapp.ability'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='personalAbility',
            field=models.ForeignKey(blank=True, default='', limit_choices_to={'type': 'personal'}, on_delete=django.db.models.deletion.CASCADE, to='feteamapp.ability'),
        ),
    ]
