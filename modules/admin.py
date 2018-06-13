# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Module


# ModelAdmin define the model behavior.
@admin.register(Module)
class ModuleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'image', 'active')
    fieldsets = (
        ('Module Info', {'fields':('name', 'url', 'order', 'image', 'active')}),
    )
    class Meta:
        model = Module