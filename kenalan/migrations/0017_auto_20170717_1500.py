# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kenalan', '0016_auto_20170717_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kenalandetail',
            name='kenalan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kenalan.Kenalan'),
        ),
    ]
