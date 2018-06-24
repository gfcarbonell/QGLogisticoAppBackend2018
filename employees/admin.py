# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'area', 'employee_type', 'employee_position', 'auth_user_profile', 
        'start_date_contract', 'end_date_contract', 'instruction_level'
    ]
    class Meta:
        model = Employee