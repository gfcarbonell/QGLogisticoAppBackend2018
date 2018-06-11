# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    fieldsets = (
        ('Menu Info', {'fields':('name', 'url')}),
    )

    class Meta:
        model = Menu