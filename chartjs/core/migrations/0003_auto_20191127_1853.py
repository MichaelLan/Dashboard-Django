# Generated by Django 2.2.7 on 2019-11-27 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191124_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='tipo_proyecto',
            field=models.CharField(max_length=30, verbose_name='Tipo de proyecto'),
        ),
    ]
