from django.shortcuts import render
from django.shortcuts import get_object_or_404


#from .models 
from .models import Theatre,Schedule,Seat

#from serializers
from .serializers import TheatreSerailaers,SeatSerializer,ScheduleSerializer

#from restframework
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from users.permissions import IsAdmin
from rest_framework import viewsets


# Create your views here.

#theatre  view for only admin
class TheatreAdminView(viewsets.ModelViewSet):

     queryset=Theatre.objects.all()
     serializer_class=TheatreSerailaers

     def get_permissions(self):
          if self.action in ['list','retrieve']:
               permission_classes = [AllowAny]
          else:
               permission_classes=[IsAuthenticated,IsAdmin]
          return [permission() for permission in permission_classes]
    


#Seat View admin 
class SeatAdminView(viewsets.ModelViewSet):
     queryset= Seat.objects.all()
     serializer_class=SeatSerializer

     def get_permissions(self):
          
          if self.action in ['list','retrieve']:
               permission_classes= [AllowAny]

          else:

               permission_classes=[IsAuthenticated,IsAdmin]
          return [permission() for permission in permission_classes]

     
     





#schedule view
class ScheduleSetUpAdminView(viewsets.ModelViewSet):

     queryset=Schedule.objects.all()
     serializer_class=ScheduleSerializer

     def get_permissions(self):
          if self.action in ['list','retrieve']:
               permission_classes = [AllowAny]
          else:
               permission_classes=[IsAuthenticated,IsAdmin]
          return [permission() for permission in permission_classes]
    


     
     


               
        
            

