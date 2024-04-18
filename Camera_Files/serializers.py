from rest_framework import serializers
from .models import Camera_Files , Gtoken

class Camera_FilesSerializer(serializers.ModelSerializer):
    camera_files_url = serializers.FileField(required=False)
    class Meta:
        model = Camera_Files
        fields = ['id', 'created_by','created_at','camera_files_url']
        read_only_fields = ['created_by']
        
class GtokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gtoken
        fields = ['gtoken' , 'created_by']
        read_only_fields = ['created_by']
                
