from django.db import models


import uuid
# Create your models here.

#user data model
from users.models import User

class Log(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    action=models.CharField(max_length=100,null=True,blank=True)
    data=models.JSONField(null=True,blank=True)
    timestampe=models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.user.name