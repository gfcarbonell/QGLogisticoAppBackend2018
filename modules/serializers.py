# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Module

# Serializers define the API representation.
class ModuleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name', 'url']
        