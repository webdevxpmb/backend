# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 13:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kenalan', '0013_auto_20170717_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kenalan',
            name='user_maba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_maba', to=settings.AUTH_USER_MODEL),
        ),
    ]
