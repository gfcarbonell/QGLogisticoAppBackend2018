# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Headquarters
from entities.models import Entity
from entities.serializers import EntityModelSerializer
from contact_information.serializers import ContactInformationModelSerializer
from extra_information.serializers import ExtraInformationModelSerializer 

# Serializers define the API representation.
class HeadquartersModelSerializer(serializers.ModelSerializer):
    contact_information =  ContactInformationModelSerializer(many=True) 
    extra_information =  ExtraInformationModelSerializer(many=True)
    class Meta:
        model = Headquarters
        fields = ['id', 'entity', 'name', 'contact_information', 'extra_information', 'active']