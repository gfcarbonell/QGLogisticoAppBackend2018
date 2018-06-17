# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import AuthUserProfile
from .serializers import AuthUserProfileModelSerializer, AuthUserProfileMainMenuModelSerializer




# ViewSets define the view behavior.
class AuthUserProfileModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AuthUserProfile.objects.all()
    serializer_class = AuthUserProfileModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^name', '^last_name', '^mother_last_name', '^auth_user__username')
    filter_fields = ('gender', 'blood_group', 'active')
    ordering_fields = ('last_name', 'mother_last_name', 'name', 'auth_user__username')


# ViewSets define the view behavior.
class AuthUserProfileMainMenuModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AuthUserProfile.objects.all()
    serializer_class = AuthUserProfileMainMenuModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^name', '^last_name', '^mother_last_name', '^auth_user__username')
    filter_field = ('active')
    ordering_field = ('auth_user__username')





