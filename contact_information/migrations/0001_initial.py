# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, help_text='Email | Correo electrónico', max_length=254, unique=True)),
                ('cell_phone', phonenumber_field.modelfields.PhoneNumberField(db_index=True, help_text='Cell phone | Celular', max_length=128, unique=True)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(db_index=True, help_text='Telephone | Teléfono', max_length=128, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Contact Information',
                'verbose_name_plural': 'Contact Information',
                'db_table': 'contact_information',
                'ordering': ['email', 'cell_phone', 'telephone'],
            },
        ),
    ]
