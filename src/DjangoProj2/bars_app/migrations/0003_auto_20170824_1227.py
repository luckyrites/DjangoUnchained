# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bars_app', '0002_bars_model_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bars_model',
            new_name='Bars_Location_Model',
        ),
    ]