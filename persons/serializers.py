# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Person
from contact_information.serializers import ContactInformationModelSerializer 
from extra_information.serializers import ExtraInformationModelSerializer


# Serializers define the API representation.
class PersonModelSerializer(serializers.ModelSerializer):
    contact_information = ContactInformationModelSerializer(many=True)
    extra_information =  ExtraInformationModelSerializer(many=True)   
    class Meta:
        model = Person
        fields = [
                    'id', 'last_name', 'mother_last_name', 'name', 'birthday', 'gender', 
                    'marital_status', 'photography', 'contact_information', 'extra_information'
                ]


