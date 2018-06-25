# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import IdentificationDocument


@admin.register(IdentificationDocument)
class IdentificationDocumentAdmin(admin.ModelAdmin):
    list_display = ['person', 'identification_document_type', 'number']
    search_fields  = ['person', 'identification_document_type', 'number', 'id']
    fieldsets = (
        ('Identification document info', {'fields':('person', 'identification_document_type', 'number',)}),
    )
    class Meta:
        model = IdentificationDocument