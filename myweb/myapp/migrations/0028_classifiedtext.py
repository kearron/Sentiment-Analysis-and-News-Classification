# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_search'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassifiedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
