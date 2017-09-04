# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 05:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items', to='bars_app.Bars_Location_Model'),
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items', to=settings.AUTH_USER_MODEL),
        ),
    ]
