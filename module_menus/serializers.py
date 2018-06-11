# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import ModuleMenu
from modules.serializers import ModuleModelSerializer
from menus.serializers import MenuModelSerializer


# Serializers define the API representation.
class ModuleMenuModelSerializer(serializers.ModelSerializer):
    module = ModuleModelSerializer()
    menu = MenuModelSerializer()
    class Meta:
        model = ModuleMenu
        fields = ['id', 'module', 'menu', 'order', 'image' ,'active']
        read_only_fields = ['module', 'menu']