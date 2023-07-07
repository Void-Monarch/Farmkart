from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username ,phone_number,email,first_name, last_name, password=None):
        if not email:
            raise ValueError("User Must have a email error")

        if not username:
            raise ValueError("user must have a username")

        user = self.model( 
            email = self.normalize_email(email),
            username = username.strip(),
            first_name = first_name.strip(),
            last_name = last_name.strip(),
            phone_number = phone_number.strip(),
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username ,phone_number,email,password,first_name="", last_name=""):
        user = self.create_user(email=self.normalize_email(email),username=username.strip(),password=password.strip(),first_name=first_name.strip(),last_name=last_name,phone_number=phone_number.strip())
        user.is_admin = True
        user.is_staff = True
        user.is_active = True   
        user.is_useradmin = True
        user.save(using=self.db)

        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    username = models.CharField(max_length=64,unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    billing_address = models.TextField(max_length=600,blank=True,null=True)

    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("email", "phone_number", )

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm: str) -> bool:
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
