# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='logo',
            field=models.ImageField(blank=True, default='images/defaults/Default-1.png', help_text='Logo | logo', null=True, upload_to='images/persons/'),
        ),
    ]
