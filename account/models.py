from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self , email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        
        user.set_password(password)
        user.save()
        
        return user
    def create_superuser(self , email ,password=None ,**extra_fields ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password)
        
class UserAccount(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=225 , unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def __str__(self):
        return self.email
    
        
    
        
