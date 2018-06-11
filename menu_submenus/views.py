# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import MenuSubMenu
from .serializers import MenuSubMenuModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class MenuSubMenuModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menu submenus to be viewed or edited.
    """
    queryset = MenuSubMenu.objects.all()
    serializer_class = MenuSubMenuModelSerializer
    permission_classes = (IsAuthenticated,)