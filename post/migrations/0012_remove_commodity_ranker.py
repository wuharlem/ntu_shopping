# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_commodity_ranker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='ranker',
        ),
    ]
