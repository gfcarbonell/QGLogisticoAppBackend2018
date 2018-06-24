# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import EntityActivity


# Serializers define the API representation.
class EntityActivityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityActivity
        fields = ['id', 'name']