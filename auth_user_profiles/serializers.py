# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import AuthUserProfile
from auth_users.serializers import AuthUserModelSerializer
from contact_information.serializers import ContactInformationModelSerializer 
from extra_information.serializers import ExtraInformationModelSerializer


# Serializers define the API representation.
class AuthUserProfileModelSerializer(serializers.ModelSerializer):
    auth_user = AuthUserModelSerializer(many=False)
    contact_information = ContactInformationModelSerializer(many=True, read_only=True)
    extra_information =  ExtraInformationModelSerializer(read_only=True)
    class Meta:
        model = AuthUserProfile
        fields = [
                    'id', 'last_name', 'mother_last_name', 'name', 'birthday', 
                    'gender', 'marital_status', 'blood_group', 'photography', 
                    'auth_user', 'contact_information', 'extra_information','active']


# Serializers define the API representation.
class AuthUserProfileMainMenuModelSerializer(serializers.ModelSerializer):
    auth_user = AuthUserModelSerializer()
    class Meta:
        model = AuthUserProfile
        fields = ['id', 'auth_user', 'photography',]


