# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_remove_employee_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='instruction_level',
            field=models.CharField(choices=[('Sin nivel', 'Sin nivel'), ('Pre escolar', 'Pre escolar'), ('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Superior', 'Superior')], help_text='Instruction level | Nivel de instrucción', max_length=12),
        ),
    ]
