# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kenalan', '0015_auto_20170717_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kenalandetail',
            name='kenalan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='kenalan.Kenalan'),
        ),
    ]
