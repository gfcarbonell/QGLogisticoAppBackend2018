# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import ModuleMenu
from .serializers import ModuleMenuModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class ModuleMenuModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menu submenus to be viewed or edited.
    """
    queryset = ModuleMenu.objects.all()
    serializer_class = ModuleMenuModelSerializer
    permission_classes = (IsAuthenticated,)