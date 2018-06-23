# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-23 16:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0004_area_dependency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='initials',
            field=models.CharField(blank=True, db_index=True, help_text='Initials | Iniciales', max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(db_index=True, help_text='Name | Nombre', max_length=100, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
