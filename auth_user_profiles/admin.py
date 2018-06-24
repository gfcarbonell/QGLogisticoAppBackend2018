# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import AuthUserProfile


@admin.register(AuthUserProfile)
class AuthUserProfileAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'birthday', 'gender', 'marital_status', 'auth_user']
    search_fields = ['name', 'last_name', 'mother_last_name', 'auth_user__username', 'id']
    filter_horizontal = ['contact_information', 'extra_information']
    fieldsets = (
        ('Headquarters Info', {'fields':('last_name', 'mother_last_name', 'name', 'birthday', 'gender', 'marital_status', 'auth_user')}),
        ('Complement Info', {'fields':('contact_information', 'extra_information')}),
    )
    class Meta:
        model = AuthUserProfile