# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import IdentificationDocumentType
from .serializers import IdentificationDocumentTypeModelSerializer


# ViewSets define the view behavior.
class IdentificationDocumentTypeModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IdentificationDocumentType.objects.all()
    serializer_class = IdentificationDocumentTypeModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^name', '^initials', '^digits')
    ordering_fields = ('name', 'initials', 'digits')