# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-08-10 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsindexpage',
            name='linkedevents_params',
            field=models.CharField(default='?keyword=yso:p8692,yso:p26655', max_length=200),
        ),
    ]
