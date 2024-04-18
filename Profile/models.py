from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model


def logo_dir_path(self, filename):
    extension = filename.split('.')[-1]
    og_filename = filename.split('.')[0]
    new_filename = "%s.%s" % (self.created_by_id, extension)

    return 'profile_image/{new_filename}'.format(new_filename=new_filename)
User = get_user_model()
class Profiles(models.Model):
    profile_image_url = models.ImageField(upload_to=logo_dir_path, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
