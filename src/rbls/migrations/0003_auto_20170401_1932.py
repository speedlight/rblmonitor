# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbls', '0002_auto_20170401_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rbllist',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
