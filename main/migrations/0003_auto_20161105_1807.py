# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161105_1739'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Graph',
            new_name='GraphModel',
        ),
    ]
