# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenalan', '0008_expiredtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
