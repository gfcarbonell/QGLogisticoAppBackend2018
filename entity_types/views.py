# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import EntityType
from .serializers import EntityTypeModelSerializer


# ViewSets define the view behavior.
class EntityTypeModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EntityType.objects.all()
    serializer_class = EntityTypeModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_field = '^name'
    ordering_fields = ('name', 'initials')