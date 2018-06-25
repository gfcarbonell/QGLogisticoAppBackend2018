# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 23:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extra_information', '0001_initial'),
        ('entities', '0001_initial'),
        ('contact_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headquarters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Name | Nombre', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)])),
                ('active', models.BooleanField(default=True, help_text='Active | Activo')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('contact_information', models.ManyToManyField(blank=True, help_text='Contact information | Informarción de contacto', to='contact_information.ContactInformation')),
                ('entity', models.ForeignKey(help_text='Entity | Entidad', on_delete=django.db.models.deletion.CASCADE, to='entities.Entity')),
                ('extra_information', models.ManyToManyField(blank=True, help_text='Extra information | Informarción extra', to='extra_information.ExtraInformation')),
            ],
            options={
                'verbose_name': 'Entity',
                'verbose_name_plural': 'Headquarters',
                'db_table': 'headquarters',
                'ordering': ['entity', 'name'],
            },
        ),
    ]