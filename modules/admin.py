# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Module


@admin.register(Module)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    fieldsets = (
        ('Module Info', {'fields':('name', 'url')}),
    )

    class Meta:
        model = Module