# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-07-19 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
