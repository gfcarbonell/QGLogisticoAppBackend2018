# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Menu
from submenus.serializers import SubMenuModelSerializer

# Serializers define the API representation.
class MenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'url']
        