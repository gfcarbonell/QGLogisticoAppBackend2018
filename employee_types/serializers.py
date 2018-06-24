# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import EmployeeType


# Serializers define the API representation.
class EmployeeTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ['id', 'name', 'initials']