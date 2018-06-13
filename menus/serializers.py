# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Menu
from modules.serializers import ModuleModelSerializer


# Serializers define the API representation.
class MenuModelSerializer(serializers.ModelSerializer):
    module = ModuleModelSerializer()
    class Meta:
        model = Menu
        fields = ['id', 'module', 'name', 'url', 'order', 'image', 'active']
        