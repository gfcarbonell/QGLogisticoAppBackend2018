# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import IdentificationDocumentType


@admin.register(IdentificationDocumentType)
class IdentificationDocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['identification_document_class', 'name', 'initials', 'digits']
    search_fields  = ['identification_document_class', 'name', 'initials','id']
    fieldsets = (
        ('Identification documentType info', {'fields':('identification_document_class', 'name', 'initials', 'digits',)}),
    )
    class Meta:
        model = IdentificationDocumentType