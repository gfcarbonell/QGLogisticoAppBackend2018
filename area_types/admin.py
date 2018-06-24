# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import AreaType


@admin.register(AreaType)
class AreaTypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'abbreviation']
	search_fields  = ['name', 'abbreviation', 'id']
	fieldsets = (
        ('Entity Type', {'fields':('name', 'abbreviation')}),
    )
	class Meta:
		model = AreaType