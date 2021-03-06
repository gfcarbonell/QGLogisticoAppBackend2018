# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_positions', '0001_initial'),
        ('employee_types', '0001_initial'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_contract', models.DateField(help_text='Start date contract | Inicio fecha contrato')),
                ('end_date_contract', models.DateField(help_text='End date contract | Fin fecha contrato')),
                ('instruction_level', models.CharField(choices=[('Sin Nivel', 'Sin Nivel'), ('Pre Escolar', 'Pre Escolar'), ('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Superior', 'Superior')], help_text='Instruction level | Nivel de instrucción', max_length=12)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], help_text='Blood group | Grupo sanguíneo', max_length=9, null=True)),
                ('active', models.BooleanField(default=True, help_text='Active | Activo')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('area', models.ForeignKey(help_text='Area | Área', on_delete=django.db.models.deletion.CASCADE, to='areas.Area')),
                ('auth_user', models.OneToOneField(help_text='Auth User | Usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('employee_position', models.ForeignKey(help_text='Employee position | Cargo de empleado', on_delete=django.db.models.deletion.CASCADE, to='employee_positions.EmployeePosition')),
                ('employee_type', models.ForeignKey(help_text='Employee type | Tipo de empleado', on_delete=django.db.models.deletion.CASCADE, to='employee_types.EmployeeType')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'emplooyes',
            },
        ),
    ]
