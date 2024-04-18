from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import Camera_FilesSerializer ,GtokenSerializer
from .models import Camera_Files , Gtoken
from rest_framework import serializers   
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
import json
from rest_framework.views import APIView  
from rest_framework import status


from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
import os
import requests
from requests.exceptions import ConnectionError, HTTPError


class GtokenViewSet(APIView):
    queryset=Gtoken.objects.all()
    serializer_class = GtokenSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]
    
    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)


    def post(self, request):
        serializer = GtokenSerializer(data = request.data)
        # print(len(Gtoken.objects.filter(created_by=self.request.user)))
        # print(request.data['gtoken'])
        if len(Gtoken.objects.filter(created_by=self.request.user))>=1:
            if serializer.is_valid():
                Gtoken.objects.filter(created_by=self.request.user).update(gtoken=request.data['gtoken'])
            # instance = Gtoken.objects.get(created_by=self.request.user)
            # print(instance)
            # instance.gtoken = request.data['gtoken']
            # insatance.save()
                return Response(serializer.data, status= status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save(created_by=self.request.user)
                return Response(serializer.data, status= status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class Camera_FileslViewSet(generics.ListCreateAPIView):
    queryset = Camera_Files.objects.all()
    serializer_class = Camera_FilesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        
class Camera_FilesApi(generics.ListAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # queryset = Todo.objects.all()
    queryset = Camera_Files.objects.all()
    serializer_class = Camera_FilesSerializer
    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Profiles.objects.all().filter(created_by= user)
    
    serializer_class = Camera_FilesSerializer

class Camera_FilesUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Camera_Files.objects.all()
    serializer_class = Camera_FilesSerializer

class Camera_FilesDeleteApi(generics.DestroyAPIView):
    queryset = Camera_Files.objects.all()
    serializer_class = Camera_FilesSerializer
    
    
    

# Optionally providing an access token within a session if you have enabled push security

# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
