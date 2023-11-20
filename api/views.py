from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from user import models
from rest_framework import generics
from . import serializers
from django.shortcuts import get_object_or_404


class UserView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [IsAuthenticated]


class SocialProfileList(generics.ListCreateAPIView):
    queryset = models.SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [IsAuthenticated]


class SocialProfileRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [IsAuthenticated]


class CredentialsList(generics.ListCreateAPIView):
    queryset = models.Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [IsAuthenticated]


class CredentialsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [IsAuthenticated]
