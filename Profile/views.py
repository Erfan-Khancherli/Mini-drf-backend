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
        if len(Profiles.objects.filter(created_by=self.request.user))>=1:
            Profiles.objects.filter(created_by=self.request.user).update(profile_image_url=request.data['profile_image_url'])
            if serializer.is_valid():
                data = {
                        "status": 200,
                        "message": "Success",
                        "data":"Updated"
                        }
                return Response(data=data, status= status.HTTP_201_CREATED,content_type='application/json')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save(created_by=self.request.user)
                return Response(serializer.data, status= status.HTTP_201_CREATED)
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