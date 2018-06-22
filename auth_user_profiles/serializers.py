# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import AuthUserProfile
from auth_users.models import AuthUser
from auth_users.serializers import AuthUserModelSerializer
from contact_information.serializers import ContactInformationModelSerializer 
from extra_information.serializers import ExtraInformationModelSerializer


# Serializers define the API representation.
class AuthUserProfileModelSerializer(serializers.ModelSerializer):
    auth_user = AuthUserModelSerializer()
    contact_information = ContactInformationModelSerializer(many=True, read_only=True)
    extra_information =  ExtraInformationModelSerializer(read_only=True)
    
    def create(self, validated_data):
        user_data = validated_data.pop('auth_user')
        username = user_data.get('username', None)
        user = AuthUserModelSerializer.create(AuthUserModelSerializer(), validated_data=user_data)
        user_profile, created = AuthUserProfile.objects.update_or_create(auth_user=user, **validated_data)
        return user_profile
     

    class Meta:
        model = AuthUserProfile
        fields = ['id', 'last_name', 'mother_last_name', 'name',
        'birthday', 'gender', 'marital_status', 'blood_group', 
        'auth_user', 'contact_information', 'extra_information', 'active']

# Serializers define the API representation.
class AuthUserProfileMainMenuModelSerializer(serializers.ModelSerializer):
    auth_user = AuthUserModelSerializer()
    class Meta:
        model = AuthUserProfile
        fields = ['id', 'auth_user', 'photography',]


