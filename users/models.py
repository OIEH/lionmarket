from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    def create_user(self, username, email, phone, address, password=None):
        if not username:
            raise ValueError('아이디는 필수입니다.')
        
        user = self.model(username=username, email=email, phone=phone, address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, phone, address, password=None):
        user = self.model(username=username, email=email, phone=phone, address=address)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        
    
class User(AbstractBaseUser):
    id=models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='아이디',max_length=30,unique=True)
    email = models.EmailField(verbose_name='이메일',max_length=255)
    phone = models.CharField(verbose_name = '전화번호', max_length=11)
    address = models.CharField(verbose_name = '주소',   max_length=200,null=True) 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    def has_perms(self, perm, obj=None):
        return True
    def has_module_perm(self, app_label):
        return True
    
    def is_staff(self):
        return self.is_admin