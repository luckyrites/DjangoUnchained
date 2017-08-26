# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bars_app', '0005_bars_location_model_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bars_location_model',
            name='cuisines',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]
