from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model

from datetime import datetime
import pytz
import jdatetime


def file_dir_path(self, filename):
    country_time_zone = pytz.timezone('Iran')
    country_time = datetime.now(country_time_zone)
    date_time = datetime.today()
    extension = filename.split('.')[-1]
    path = "%s" % (self.created_by_id)
    new_filename = "%s_%s.jpeg" % (country_time.strftime('%d-%m-%y') ,country_time.strftime('%H:%M:%S') )
    return 'Files/{path}/{new_filename}'.format(path=path ,new_filename=new_filename )

User = get_user_model()
class Camera_Files(models.Model):
    created_by= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    camera_files_url= models.FileField(upload_to=file_dir_path, blank=True,null=True,)

class Gtoken(models.Model):
    gtoken = models.CharField(default='0')
    created_by= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)