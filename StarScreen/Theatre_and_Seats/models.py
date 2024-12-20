from django.db import models
from django.core.exceptions import ValidationError

#from python

import uuid


#from movie app
from movie.models import Movie
#from tickets app

# Create your models here.


# data table for Theatre
class Theatre(models.Model):


    #Screeen Types 
    list_screen_types = [
    ("Standard", "Standard Screen"),
    ("IMAX", "IMAX Screen"),
    ("Dolby", "Dolby Cinema Screen"),
    ("3D", "3D Screen"),
    ("4DX", "4DX Screen"),
    ]


    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    theatre_name=models.CharField(max_length=100,null=True,blank=True)
    theatre_location=models.CharField(max_length=300,null=True,blank=True)
    theatre_capacity=models.IntegerField(default=200)
    screen_types=models.CharField(max_length=30,choices=list_screen_types)
    


    def __str__(self):
        return self.theatre_name
    

#data table for seat
class Seat(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    seat_no=models.CharField(max_length=5,null=True,blank=True)
    theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE)
    row=models.CharField(max_length=5,null=True,blank=True)
    is_available=models.BooleanField(default=True)



    def __str__(self):

        return f'{self.seat_no}'




#Schedule data table

class Schedule(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE,null=True,blank=True)
    seat=models.ForeignKey(Seat,on_delete=models.CASCADE,null=True,blank=True)
    start_time=models.TimeField()
    end_time=models.TimeField()
    date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.movie.title} on {self.date} at {self.start_time} to {self.end_time}"


    
            




    





    


