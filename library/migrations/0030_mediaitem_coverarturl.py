# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-26 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0029_remove_mediaitem_coverart'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaitem',
            name='coverArtUrl',
            field=models.CharField(default='', max_length=200),
        ),
    ]