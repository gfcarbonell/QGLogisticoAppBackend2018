# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeModelSerializer 


# ViewSets define the view behavior.
class EmployeeModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^person__name', '^person__last_name', '^person__mother_last_name', '^auth_user__username')
    filter_fields = ('person__gender', 'person__marital_status', 'active')
    ordering_fields = ('person__last_name', 'person__mother_last_name', 'person__name', 'auth_user__username')