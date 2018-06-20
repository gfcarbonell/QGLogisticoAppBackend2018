# -*- encoding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import AuthUser


# Serializers define the API representation.
class AuthUserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'}, allow_blank=False, write_only=True)
    
    def validate(self, data):
        """
            Checks to be sure that the received password and confirm_password
            fields are exactly the same
        """
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError('Las contraseñas no coinciden')
        return data

    def create(self, validated_data):
        user = super(AuthUserModelSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(AuthUserModelSerializer, self).update(instance, validated_data)
        if validated_data['password']:
            user.set_password(validated_data['password'])
        user.save()
        return user   

    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'password', 'confirm_password','email', 'is_active', 'is_superuser' ]
        read_only_fields = ['is_active', 'is_staff', 'is_superuser', 'data_joined']
        write_only_fields = ['password', 'confirm_password']

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permission
		fields = '__all__'

class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')