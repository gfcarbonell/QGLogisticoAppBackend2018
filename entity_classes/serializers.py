# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import EntityClass


# Serializers define the API representation.
class EntityClassModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityClass
        fields = ['id', 'entity_scope', 'name']