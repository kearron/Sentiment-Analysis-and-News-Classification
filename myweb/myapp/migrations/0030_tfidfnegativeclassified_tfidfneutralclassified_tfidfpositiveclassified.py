# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_auto_20170805_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='tfidfNegativeClassified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('pubDate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tfidfNeutralClassified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('pubDate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tfidfPositiveClassified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('pubDate', models.CharField(max_length=20)),
            ],
        ),
    ]