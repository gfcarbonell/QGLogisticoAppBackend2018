# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identification_document_types', '0001_initial'),
        ('identification_documents', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='identification_document_type',
            field=models.ManyToManyField(through='identification_documents.IdentificationDocument', to='identification_document_types.IdentificationDocumentType'),
        ),
    ]
