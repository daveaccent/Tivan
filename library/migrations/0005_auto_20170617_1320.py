# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-17 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_videogame_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogame',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='slug',
        ),
    ]
