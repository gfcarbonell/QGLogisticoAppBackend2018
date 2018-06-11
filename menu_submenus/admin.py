# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import MenuSubMenu


@admin.register(MenuSubMenu)
class MenuSubMenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'submenu', 'order', 'image', 'active')
    class Meta:
        model = MenuSubMenu