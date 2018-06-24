# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import EntityClass
from .serializers import EntityClassModelSerializer


# ViewSets define the view behavior.
class EntityClassModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EntityClass.objects.all()
    serializer_class = EntityClassModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_field = '^name'
    ordering_fields = ('entity_scope', 'name')