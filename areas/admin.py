# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'nominal_organic_structure_type', 'headquarters', 'initials', 'telephone_annex', 'fax', 'logo', 'active']
    search_fields  = ['headquarters', 'name', 'id']
    fieldsets = (
        ('Area Info', {'fields':('nominal_organic_structure_type', 'headquarters', 'name', 'initials', 'telephone_annex', 'fax', 'logo')}),
        ('Permissions', {'fields':('active',)}),
    )
    class Meta:
        model = Area