# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topperApp', '0005_genre_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='addalbum',
            name='image',
            field=models.ImageField(default='profile_images/blank.png', upload_to='album_images'),
        ),
    ]
