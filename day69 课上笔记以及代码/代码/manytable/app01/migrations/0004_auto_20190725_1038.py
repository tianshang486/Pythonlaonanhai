# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-07-25 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190725_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='good',
            field=models.IntegerField(default=1),
        ),
    ]
