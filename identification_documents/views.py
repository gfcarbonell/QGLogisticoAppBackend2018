# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import IdentificationDocument
from .serializers import IdentificationDocumentModelSerializer


# ViewSets define the view behavior.
class IdentificationDocumentModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IdentificationDocument.objects.all()
    serializer_class = IdentificationDocumentModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('identification_document_type__name', 'person__gender', 'person__marital_status',)
    search_fields = ('^person__last_name', '^person__mother_last_name', 'person__name', '^number',)
    ordering_fields = ('person__last_name', 'person__mother_last_name', 'person__name', 'number',)