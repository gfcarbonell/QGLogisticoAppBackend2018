# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Employee
from areas.models import Area
from areas.serializers import AreaModelSerializer 
from auth_users.serializers import AuthUserModelSerializer 
from persons.serializers import PersonModelSerializer 
from employee_types.models import EmployeeType
from employee_types.serializers import EmployeeTypeModelSerializer
from employee_positions.models import EmployeePosition
from employee_positions.serializers import EmployeePositionModelSerializer

# Serializers define the API representation.
class EmployeeModelSerializer(serializers.ModelSerializer):
    area = AreaModelSerializer(read_only=True)
    area_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Area.objects.all(), source='area')
    auth_user = AuthUserModelSerializer()
    person = PersonModelSerializer()
    employee_position = EmployeePositionModelSerializer(read_only=True)
    employee_position_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=EmployeePosition.objects.all(), source='employee_position')
    employee_type = EmployeeTypeModelSerializer(read_only=True)
    employee_type_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=EmployeeType.objects.all(), source='employee_type')
    
    def create(self, validated_data):
        person_data = validated_data.pop('person')
        person = PersonModelSerializer.create(PersonModelSerializer(), validated_data=person_data)

        user_data = validated_data.pop('auth_user')
        user = AuthUserModelSerializer.create(AuthUserModelSerializer(), validated_data=user_data)

        employee, created = Employee.objects.update_or_create(person=person, auth_user=user, **validated_data)
        return employee

    class Meta:
        model = Employee
        fields = [
            'id', 'area', 'area_id', 'employee_type', 'employee_type_id', 'employee_position', 'employee_position_id', 'person', 
            'start_date_contract', 'end_date_contract', 
            'instruction_level', 'auth_user', 'active'
        ]