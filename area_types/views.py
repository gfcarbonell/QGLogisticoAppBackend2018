# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import AreaType
from .serializers import AreaTypeModelSerializer


# ViewSets define the view behavior.
class AreaTypeModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_field = '^name'
    ordering_fields = ('name', 'initials')