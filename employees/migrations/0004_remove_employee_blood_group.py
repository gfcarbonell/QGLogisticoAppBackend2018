# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20180624_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='blood_group',
        ),
    ]
