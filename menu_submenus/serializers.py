# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import MenuSubMenu
from menus.serializers import MenuModelSerializer
from submenus.serializers import SubMenuModelSerializer


# Serializers define the API representation.
class MenuSubMenuModelSerializer(serializers.ModelSerializer):
    menu = MenuModelSerializer()
    submenu = SubMenuModelSerializer()
    class Meta:
        model = MenuSubMenu
        fields = ['id', 'menu', 'submenu', 'order', 'image' ,'active']
        read_only_fields = ['menu', 'submenu']
        