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
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin


# Create your views here.

#theatre  view for only admin
class TheatreAdminView(GenericAPIView):

    serializer_class=TheatreSerailaers
    permission_classes=[IsAuthenticated,IsAdmin]

    def post(self,request):

        data=request.data

        serializer=TheatreSerailaers(data=data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    def put(self,request,pk):
         
        try:
             theatre=get_object_or_404(Theatre,id=pk)
        except Theatre.DoesNotExist:
             
             return Response({"message":"Couldn't be found"})
        
        serializer=TheatreSerailaers(theatre,data=request.data)

        if serializer.is_valid():
             
             serializer.save()

             return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
         
        try:
             theatre=get_object_or_404(Theatre,id=pk)
        except Theatre.DoesNotExist:
             
             return Response({"message":"Couldn't be found"})
        
        serializer=TheatreSerailaers(theatre,data=request.data,partial=True)

        if serializer.is_valid():
             
             serializer.save()

             return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
         
        try:
             theatre=get_object_or_404(Theatre,id=pk)
        except Theatre.DoesNotExist:
             
             return Response({"message":"Couldn't be found"})
        
        theatre.delete()
        return Response({"message":"Item successfully deleted"})
        

        


    

#theatre get view general purpose
class TheatreListView(GenericAPIView):

    serializer_class=TheatreSerailaers
    permission_classes=[IsAuthenticated]

    def get(self,request):

            theatres=Theatre.objects.all()

            if theatres:

                serializer=TheatreSerailaers(theatres,many=True)

                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#theatre detail view
class TheaterDetailsView(GenericAPIView):
     
    serializer_class=TheatreSerailaers
    permission_classes=[IsAuthenticated]


    def get(self,request,pk):
         
        try:
             theatre=get_object_or_404(Theatre,id=pk)
        except Theatre.DoesNotExist:
             
             return Response({"message":"Couldn't be found"})
        

        serializer=TheatreSerailaers(theatre,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK) 


            


#Seat View admin 
class SeatAdminView(GenericAPIView):
     
     serializer_class=SeatSerializer
     permission_classes=[IsAuthenticated,IsAdmin]

     def post(self,request):
          
          data=request.data

          serializer=SeatSerializer(data=data)

          if serializer.is_valid():
               
               serializer.save()

               return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

     def put(self,request,pk):
          
        try:
            seat=get_object_or_404(Seat,id=pk)
        except Seat.DoesNotExist:
             return Response({"message":"Couldn't be found"})
        
        serializer=SeatSerializer(seat,data=request.data)

        if serializer.is_valid():
             
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

     def patch(self,request,pk):
          
        try:
            seat=get_object_or_404(Seat,id=pk)
        except Seat.DoesNotExist:
             return Response({"message":"Couldn't be found"})
        
        serializer=SeatSerializer(seat,data=request.data,partial=True)

        if serializer.is_valid():
             
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

     def delete(self,request,pk):
         
        try:
             seat=get_object_or_404(Seat,id=pk)
        except Seat.DoesNotExist:
             
             return Response({"message":"Couldn't be found"})
        
        seat.delete()
        return Response({"message":"Item successfully deleted"})
     


#seat list view
class SeatListView(GenericAPIView):
     
    permission_classes=[IsAuthenticated]
    serializer_class=SeatSerializer

    def get(self,request):
          
        seats=Seat.objects.all()

        if seats:
               
            serializer=SeatSerializer(seats,many=True)

            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


#seat detail view
class SeatDetailsView(GenericAPIView):
     
    serializer_class=SeatSerializer
    permission_classes=[IsAuthenticated]


    def get(self,request,pk):
         
        try:
             seat=get_object_or_404(Seat,id=pk)
        except Seat.DoesNotExist:
             
             return Response({"message":"Couldn't be found"})
        

        serializer=TheatreSerailaers(seat,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

#schedule view
class ScheduleSetUpAdminView(GenericAPIView):

     serializer_class=ScheduleSerializer
     permission_classes=[IsAuthenticated,IsAdmin]


     def post(self,request):

          data=request.data

          serializer=ScheduleSerializer(data=data)

          if serializer.is_valid():

               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     


     def put(self,request,pk):
          
        try:
            schedule=get_object_or_404(Schedule,id=pk)
        except Schedule.DoesNotExist:
             return Response({"message":"Couldn't be found"})
        
        serializer=ScheduleSerializer(schedule,data=request.data)

        if serializer.is_valid():
             
             serializer.save()
             return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

     def patch(self,request,pk):
          
        try:
            schedule=get_object_or_404(Schedule,id=pk)
        except Schedule.DoesNotExist:
             return Response({"message":"Couldn't be found"})
        
        serializer=ScheduleSerializer(schedule,data=request.data,partial=True)

        if serializer.is_valid():
             
             serializer.save()
             return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

     def delete(self,request,pk):
         
        try:
             schedule=get_object_or_404(Schedule,id=pk)
        except Schedule.DoesNotExist:
             
             return Response({"message":"Couldn't be found"})
        
        schedule.delete()
        return Response({"message":"Item successfully deleted"})
               
        
            

