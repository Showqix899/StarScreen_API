from django.db import models


##
import uuid

# Create your models here.

#import model from Theater_and_Seats
from Theatre_and_Seats.models import Theatre,Schedule,Seat

#import model from User
from users.models import User

#import model from Movie
from movie.models import Movie






class Ticket(models.Model):

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    assigned_to=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE,null=True,blank=True)
    seat_no=models.ForeignKey(Seat,on_delete=models.CASCADE,null=True,blank=True)
    schedule=models.ForeignKey(Schedule,on_delete=models.CASCADE,null=True,blank=True)
    movie=models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    purchased_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return f'ticket no {self.id} of {self.theatre} at seat no {self.seat_no}'