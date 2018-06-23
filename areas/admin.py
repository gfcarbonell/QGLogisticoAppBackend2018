# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['headquarters', 'dependency', 'name', 'nominal_organic_structure_type', 'initials', 'telephone_annex', 'fax', 'logo', 'active']
    search_fields  = ['headquarters', 'name', 'id']
    fieldsets = (
        ('Area Info', {'fields':('dependency', 'nominal_organic_structure_type', 'headquarters', 'name', 'initials', 'telephone_annex', 'fax', 'logo')}),
        ('Permissions', {'fields':('active',)}),
    )
    class Meta:
        model = Area