from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ProfilesSerializer
from .models import Profiles
from rest_framework import serializers   
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
import json
from rest_framework.views import APIView  
from rest_framework import status

class ProfileslViewSet(APIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = ProfilesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProfilesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
class ProfilesApi(generics.ListAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # queryset = Todo.objects.all()
    # queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    def get_queryset(self):
        user = self.request.user
        return Profiles.objects.filter(created_by= user)
    
    serializer_class = ProfilesSerializer

class ProfilesUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer

class ProfilesDeleteApi(generics.DestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
