# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars_app', '0007_auto_20170824_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bars_location_model',
            name='cuisines',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]