# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import Module
from .serializers import ModuleModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class ModuleModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows modules to be viewed or edited.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleModelSerializer
    permission_classes = (IsAuthenticated,)