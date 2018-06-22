# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Entity


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
	list_display = [ 'name', 'entity_class', 'entity_type', 'entity_activity','slogan', 'initials', 'logo', 'active']
	search_fields  = ['name', 'initials', 'id']
	fieldsets = (
        ('Entity Info', {'fields':('entity_class', 'entity_type', 'entity_activity', 'name', 'slogan', 'initials', 'logo')}),
		('Permissions', {'fields':('active',)}),
	)
	class Meta:
		model = Entity