# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20170730_0348'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NegativeClassified',
        ),
        migrations.DeleteModel(
            name='NeutralClassified',
        ),
        migrations.DeleteModel(
            name='newsType',
        ),
        migrations.DeleteModel(
            name='PositiveClassified',
        ),
    ]