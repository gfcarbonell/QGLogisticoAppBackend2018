# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import EmployeePosition


# Serializers define the API representation.
class EmployeePositionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePosition
        fields = ['id', 'name', 'abbreviation']