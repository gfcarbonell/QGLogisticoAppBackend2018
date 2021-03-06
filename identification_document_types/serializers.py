# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import IdentificationDocumentType


# Serializers define the API representation.
class IdentificationDocumentTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationDocumentType
        fields = [
                    'id', 'identification_document_class', 'name', 'initials', 'digits'
                ]