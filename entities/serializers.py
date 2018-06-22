# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Entity


# Serializers define the API representation.
class EntityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ['id', 'entity_class', 'entity_type', 'entity_activity', 'name', 'slogan', 'initials', 'logo']