# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Headquarters


@admin.register(Headquarters)
class HeadquartersAdmin(admin.ModelAdmin):
    list_display = [ 'entity', 'name', 'active']
    search_fields  = ['entity', 'name', 'id']
    filter_horizontal = ['contact_information', 'extra_information']
    fieldsets = (
        ('Headquarters Info', {'fields':('entity', 'name')}),
        ('Complement Info', {'fields':('contact_information', 'extra_information')}),
        ('Permissions', {'fields':('active',)}),
    )
    class Meta:
        model = Headquarters