# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Area


# Serializers define the API representation.
class AreaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
                    'id', 'headquarters', 'area_type', 'dependency', 
                    'name', 'initials', 'nominal_organic_structure_type', 
                    'telephone_annex', 'fax', 'logo', 'active']