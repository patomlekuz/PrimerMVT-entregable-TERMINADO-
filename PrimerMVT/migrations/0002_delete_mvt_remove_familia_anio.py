# Generated by Django 4.1 on 2022-08-21 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrimerMVT', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mvt',
        ),
        migrations.RemoveField(
            model_name='familia',
            name='anio',
        ),
    ]