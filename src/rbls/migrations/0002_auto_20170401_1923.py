# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rbllist',
            old_name='nanme',
            new_name='name',
        ),
    ]