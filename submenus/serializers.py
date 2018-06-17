# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import SubMenu
from menus.views import MenuModelSerializer

# Serializers define the API representation.
class SubMenuModelSerializer(serializers.ModelSerializer):
    menu = MenuModelSerializer()
    class Meta:
        model = SubMenu
        fields = ['id', 'menu', 'name', 'url', 'order', 'image', 'active']