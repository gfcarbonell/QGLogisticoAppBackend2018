# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'birthday', 'gender', 'marital_status', 'photography',]
    search_fields = ['name', 'last_name', 'mother_last_name', 'id']
    filter_horizontal = ['contact_information', 'extra_information',]
    fieldsets = (
        ('Person Info', {'fields':('last_name', 'mother_last_name', 'name', 'birthday', 'gender', 'marital_status')}),
        ('Complement Info', {'fields':('contact_information', 'extra_information')}),
    )
    class Meta:
        model = Person