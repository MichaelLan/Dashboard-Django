# Generated by Django 2.2.7 on 2019-12-02 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191201_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='slug',
            new_name='slug_localidad',
        ),
    ]
