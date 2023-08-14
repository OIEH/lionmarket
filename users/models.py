from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    def _create_user(self, username, email, password, phone, address,**extra_fields):
        if not username:
            raise ValueError('아이디는 필수입니다.')
        if not phone:
            raise ValueError('전화번호는 필수입니다.')
        user = self.model(username=username, email=email, phone=phone, address=address,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, username, email=None, password=None, phone=None, address=None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(username, email, password, phone, address,**extra_fields)
    

    def create_superuser(self, username, email=None, password=None,phone=None, address=None, **extra_fields ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        return self._create_user(username, email, password,phone, address, **extra_fields)
    
class User(AbstractBaseUser):
    username = models.CharField(verbose_name='아이디',max_length=30,unique=True)
    email = models.EmailField(verbose_name='이메일',max_length=255)
    phone = models.CharField(verbose_name = '전화번호', max_length=11)
    address = models.CharField(verbose_name = '주소',   max_length=200,null=True) 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    def is_staff(self):
        return self.is_admin