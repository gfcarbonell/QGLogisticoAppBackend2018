# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import ModuleMenu


@admin.register(ModuleMenu)
class ModuleMenuAdmin(admin.ModelAdmin):
    list_display = ('module', 'menu', 'order', 'image', 'active')
    class Meta:
        model = ModuleMenu