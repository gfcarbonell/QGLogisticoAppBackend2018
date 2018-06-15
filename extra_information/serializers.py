# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import ExtraInformation


# Serializers define the API representation.
class ExtraInformationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInformation
        fields = ['id', 'description', 'observation']