# Generated by Django 2.2.7 on 2019-12-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191203_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='slug_localidad',
            field=models.SlugField(verbose_name='Slug Localidad'),
        ),
    ]
