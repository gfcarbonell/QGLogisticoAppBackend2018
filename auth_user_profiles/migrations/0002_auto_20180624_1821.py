# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 23:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extra_information', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_user_profiles', '0001_initial'),
        ('contact_information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuserprofile',
            name='auth_user',
            field=models.OneToOneField(help_text='Auth user | Usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='authuserprofile',
            name='contact_information',
            field=models.ManyToManyField(blank=True, help_text='Contact information | Informarción de contacto', to='contact_information.ContactInformation'),
        ),
        migrations.AddField(
            model_name='authuserprofile',
            name='extra_information',
            field=models.ManyToManyField(blank=True, help_text='Extra information | Informarción extra', to='extra_information.ExtraInformation'),
        ),
    ]
