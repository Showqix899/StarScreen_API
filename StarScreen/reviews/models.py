from django.db import models

import uuid
#import model from User
from users.models import User

#import model from movie
from movie.models import Movie

#data table for user review
class Review(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    review=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):

        return f'review of {self.user.name}'
