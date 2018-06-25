# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Employee


# Serializers define the API representation.
class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id', 'area', 'employee_type', 'employee_position', 'person', 
            'start_date_contract', 'end_date_contract', 
            'instruction_level', 'auth_user', 'active'
        ]