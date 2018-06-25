# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import IdentificationDocument


# Serializers define the API representation.
class IdentificationDocumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationDocument
        fields = [
                    'id', 'person', 'identification_document_type', 'number'
                ]