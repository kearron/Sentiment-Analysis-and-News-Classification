# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_negativeclassified_neutralclassified_positiveclassified'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NegativeClassified',
        ),
        migrations.DeleteModel(
            name='NeutralClassified',
        ),
        migrations.DeleteModel(
            name='PositiveClassified',
        ),
    ]