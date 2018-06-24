# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Headquarters
from .serializers import HeadquartersModelSerializer


# ViewSets define the view behavior.
class HeadquartersModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Headquarters.objects.all()
    serializer_class = HeadquartersModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_field = '^name'
    filter_fields = ('entity', 'active')
    ordering_field = 'name'