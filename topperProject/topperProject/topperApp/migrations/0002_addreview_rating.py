# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 16:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topperApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addreview',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
