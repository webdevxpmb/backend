# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import kenalan.models


class Migration(migrations.Migration):

    dependencies = [
        ('kenalan', '0003_auto_20170617_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='end_time',
            field=models.DateTimeField(default=kenalan.models.default_end_time),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.IntegerField(unique=True),
        ),
    ]
