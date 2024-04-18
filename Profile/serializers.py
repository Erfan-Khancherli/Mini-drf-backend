from rest_framework import serializers
from .models import Profiles

class ProfilesSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.ImageField(required=False)
    class Meta:
        model = Profiles
        fields = ['id', 'created_by','profile_image_url']
        read_only_fields = ['created_by']