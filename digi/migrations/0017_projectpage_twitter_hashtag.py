# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-16 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0016_auto_20170421_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='twitter_hashtag',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]