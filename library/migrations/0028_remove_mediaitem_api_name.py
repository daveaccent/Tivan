# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0027_auto_20170819_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediaitem',
            name='api_name',
        ),
    ]