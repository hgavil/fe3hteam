# Generated by Django 4.1.5 on 2023-01-13 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feteamapp', '0013_unitclass_proficiencies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitclass',
            name='proficiencies',
        ),
        migrations.CreateModel(
            name='Proficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profIdentifier', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('prof', models.CharField(choices=[('sword', 'Sword'), ('lance', 'Lance'), ('axe', 'Axe'), ('bow', 'Bow'), ('brawl', 'Brawl'), ('reason', 'Reason'), ('faith', 'Faith'), ('authority', 'Authority'), ('riding', 'Riding'), ('flying', 'Flying'), ('armor', 'Armor')], max_length=20)),
                ('level', models.CharField(choices=[('e', 'E'), ('e+', 'E+'), ('d', 'D'), ('d+', 'D+'), ('c,', 'C'), ('c+', 'C+'), ('b', 'B'), ('b+', 'B+'), ('a', 'A'), ('a+', 'A+'), ('s', 'S'), ('s+', 'S+'), ('mastery', 'Mastery'), ('bud', 'Budding Talent')], max_length=20)),
                ('charex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feteamapp.unit')),
                ('classex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feteamapp.unitclass')),
            ],
        ),
    ]
