# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.5 on 2017-10-25 10:12
=======
# Generated by Django 1.11.5 on 2017-10-30 07:33
>>>>>>> Add banner lifts to HelsinkiOppiiIndexPage
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('helsinkioppii', '0004_remove_case_lift_icon_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='helsinkioppiiindexpage',
            name='banner_lifts',
            field=wagtail.wagtailcore.fields.StreamField((('banner', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(max_length=120)), ('abstract', wagtail.wagtailcore.blocks.TextBlock(max_length=225)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock())))),), blank=True),
        ),
    ]
