# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-23 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.TextField(blank=True),
        ),
    ]
