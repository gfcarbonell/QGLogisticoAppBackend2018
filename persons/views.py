# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Person
from .serializers import PersonModelSerializer




# ViewSets define the view behavior.
class PersonModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^name', '^last_name', '^mother_last_name')
    filter_fields = ('gender', 'marital_status')
    ordering_fields = ('last_name', 'mother_last_name', 'name')