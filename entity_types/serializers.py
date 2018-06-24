# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import EntityType


# Serializers define the API representation.
class EntityTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ['id', 'name', 'initials']