# Generated by Django 4.1.5 on 2023-01-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0004_unitclass_classabs'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='ability',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='unit',
            name='exclusiveAbilities',
            field=models.ManyToManyField(related_name='charex', to='feteamapp.ability'),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='classAbs',
            field=models.ManyToManyField(blank=True, to='feteamapp.ability'),
        ),
    ]