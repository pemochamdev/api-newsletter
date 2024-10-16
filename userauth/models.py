from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    
    
    def create_user(self,email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("L'utlisateur doit fournie une addresse mail"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email, password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('active',True)
        extra_fields.setdefault('is_superuser',True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Le superutilisateur doit avoir is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Le superutilisateur doit avoir is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects  = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username'
    
    def __str__(self):
        return self.email
    