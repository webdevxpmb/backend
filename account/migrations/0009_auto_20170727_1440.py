# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 14:40
from __future__ import unicode_literals

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20170727_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to='', verbose_name='media'),
        ),
    ]