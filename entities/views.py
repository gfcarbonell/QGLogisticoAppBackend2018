# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Entity
from .serializers import EntityModelSerializer


# ViewSets define the view behavior.
class EntityModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entity.objects.all()
    serializer_class = EntityModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^name', '^initials')
    filter_fields = ('entity_class', 'entity_type', 'entity_activity', 'main')
    ordering_fields = ('name', 'initials')