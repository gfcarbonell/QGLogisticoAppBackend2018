# -*- encoding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import AuthUser


# Serializers define the API representation.
class AuthUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'password', 'email', 'is_active' ]
        read_only_fields = ['is_staff', 'is_superuser', 'is_active', 'data_joined']
        write_only_fields = ['password']
        
    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(AuthUserModelSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

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