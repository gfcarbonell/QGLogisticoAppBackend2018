# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import ContactInformation
from .serializers import ContactInformationModelSerializer


# ViewSets define the view behavior.
class ContactInformationModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationModelSerializer
    permission_classes = (IsAuthenticated,)