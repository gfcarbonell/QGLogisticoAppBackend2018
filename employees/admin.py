# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Employee

    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'area', 'employee_type', 'employee_position', 'person', 
        'start_date_contract', 'end_date_contract', 
        'instruction_level', 'auth_user', 'active'
    ]
    fieldsets = (
        ('Employee Info', {'fields':('area', 'employee_type', 'employee_position', 'start_date_contract', 'end_date_contract',)}),
        ('Person Info', {'fields':('person', 'instruction_level',)}),
        ('User', {'fields':('auth_user',)}),
        ('Permissions', {'fields':('active',)}),
    )
    class Meta:
        model = Employee