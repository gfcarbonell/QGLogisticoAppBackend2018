# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Area
from .serializers import AreaModelSerializer


# ViewSets define the view behavior.
class AreaModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Area.objects.all()
    serializer_class = AreaModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^name', '^initials')
    filter_fields = ('headquarters', 'dependency', 'area_type', 'nominal_organic_structure_type', 'active')
    ordering_fields = ('name', 'initials')