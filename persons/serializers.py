# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Person
from contact_information.models import ContactInformation
from contact_information.serializers import ContactInformationModelSerializer 
from extra_information.models import ExtraInformation
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

    def create(self, validated_data):
        contact_information_data = validated_data.pop('contact_information')
        contact_information = ContactInformationModelSerializer.create(ContactInformationModelSerializer(), validated_data=contact_information)

        extra_information_data = validated_data.pop('extra_information')
        extra_information = ExtraInformationModelSerializer.create(ExtraInformationModelSerializer(), validated_data=extra_information_data)

        person, created = Person.objects.update_or_create(contact_information=contact_information, extra_information=extra_information, **validated_data)
        return person

