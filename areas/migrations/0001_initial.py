# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 22:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('headquarterses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Name | Nombre', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)])),
                ('initials', models.CharField(blank=True, db_index=True, help_text='Initials | Iniciales', max_length=20, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20)])),
                ('telephone_annex', models.PositiveSmallIntegerField(default=0, help_text='Telephone annex | Anexo telefónica', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('fax', models.PositiveSmallIntegerField(default=0, help_text='Fax | Fax', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('logo', models.ImageField(blank=True, default='images/defaults/Default-1.png', help_text='Logo | logo', null=True, upload_to='images/areas/')),
                ('active', models.BooleanField(default=True, help_text='Active | Activo')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('headquarters', models.ForeignKey(help_text='Headquarters | sede', on_delete=django.db.models.deletion.CASCADE, to='headquarterses.Headquarters')),
            ],
            options={
                'verbose_name': 'Area',
                'ordering': ['headquarters', 'name', 'initials'],
                'db_table': 'areas',
                'verbose_name_plural': 'Areas',
            },
        ),
    ]
