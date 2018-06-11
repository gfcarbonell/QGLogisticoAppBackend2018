# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import SubMenu


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    fieldsets = (
        ('SubMenu Info', {'fields':('name', 'url')}),
    )

    class Meta:
        model = SubMenu