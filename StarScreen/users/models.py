from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
import uuid

# Create your models here.
#custom usermanager
class UserManager(BaseUserManager):

    #for user
    def create_user(self,email,password=None,**extra_fields):

        #checking for email
        if not email:
            raise ValueError("this Email field must be set")
        
        email = self.normalize_email(email) #normalizeing the email
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_verified',False)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    


    #for superuser  
    def create_superuser(self,email,password=None,**extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

         # Validating the fields for superuser
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    


#custom user model
class User(AbstractBaseUser,PermissionsMixin):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=255)
    porfile_pic=models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=13,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    role=models.CharField(max_length=10,choices=(('user','user'),('admin','admin')) ,default='user')
    is_verified = models.BooleanField(default=False) 
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    objects=UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name} ({self.email})"

