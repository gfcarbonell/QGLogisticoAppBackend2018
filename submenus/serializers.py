# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import SubMenu


# Serializers define the API representation.
class SubMenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['id', 'name', 'url']