# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import SubMenu


# ModelAdmin define the model behavior.
@admin.register(SubMenu)
class SubMenuModelAdmin(admin.ModelAdmin):
    list_display = ('menu', 'name', 'url', 'order', 'image', 'active')
    fieldsets = (
        ('SubMenu Info', {'fields':('menu', 'name', 'url', 'order', 'image', 'active')}),
    )

    class Meta:
        model = SubMenu