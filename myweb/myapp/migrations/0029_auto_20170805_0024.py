# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_classifiedtext'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PositiveClassified',
            new_name='naiveNegativeClassified',
        ),
        migrations.RenameModel(
            old_name='NegativeClassified',
            new_name='naiveNeutralClassified',
        ),
        migrations.RenameModel(
            old_name='NeutralClassified',
            new_name='naivePositiveClassified',
        ),
    ]
