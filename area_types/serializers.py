# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import AreaType


# Serializers define the API representation.
class AreaTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaType
        fields = ['id', 'name', 'abbreviation']