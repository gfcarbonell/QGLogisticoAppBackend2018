# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import ContactInformation


# Serializers define the API representation.
class ContactInformationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = ['id', 'email', 'cell_phone', 'telephone']