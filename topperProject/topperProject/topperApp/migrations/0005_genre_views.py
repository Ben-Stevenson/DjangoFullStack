# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topperApp', '0004_remove_addalbum_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]