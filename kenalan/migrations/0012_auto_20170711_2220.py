# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kenalan', '0011_delete_expiredtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='angkatan',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Angkatan',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
