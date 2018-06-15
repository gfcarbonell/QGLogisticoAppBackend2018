# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import ExtraInformation
from .serializers import ExtraInformationModelSerializer


# ViewSets define the view behavior.
class ExtraInformationModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExtraInformation.objects.all()
    serializer_class = ExtraInformationModelSerializer
    permission_classes = (IsAuthenticated,)