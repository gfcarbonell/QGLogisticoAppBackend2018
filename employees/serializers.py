# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Employee
from auth_users.serializers import AuthUserModelSerializer 
from persons.serializers import PersonModelSerializer 



# Serializers define the API representation.
class EmployeeModelSerializer(serializers.ModelSerializer):
    auth_user = AuthUserModelSerializer()
    person = PersonModelSerializer()

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
            'id', 'area', 'employee_type', 'employee_position', 'person', 
            'start_date_contract', 'end_date_contract', 
            'instruction_level', 'auth_user', 'active'
        ]