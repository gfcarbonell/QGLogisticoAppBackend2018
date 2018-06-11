# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import Menu
from .serializers import MenuModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class MenuModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuModelSerializer
    permission_classes = (IsAuthenticated,)