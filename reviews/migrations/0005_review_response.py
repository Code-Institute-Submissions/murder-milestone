# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-28 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20200425_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='response',
            field=models.TextField(default=''),
        ),
    ]