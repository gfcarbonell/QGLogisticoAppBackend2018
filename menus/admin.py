# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Menu


# ModelAdmin define the model behavior.
@admin.register(Menu)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('module', 'name', 'url', 'order', 'image', 'main','active')
    fieldsets = (
        ('Menu Info', {'fields':('module', 'name', 'url', 'order', 'image', 'main', 'active')}),
    )

    class Meta:
        model = Menu