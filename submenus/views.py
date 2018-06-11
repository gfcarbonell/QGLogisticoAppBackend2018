# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import SubMenu
from .serializers import SubMenuModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class SubMenuModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows submenus to be viewed or edited.
    """
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuModelSerializer
    permission_classes = (IsAuthenticated,)