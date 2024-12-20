from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import get_object_or_404


#rest framework
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


#from app
from .serializers import TicketSerializers
from .models import Ticket


#from users permission
from users.permissions import IsAdmin


# Create your views here.

#for generate tickets

#A viewset for viewing, creating, updating, and deleting tickets.
class TicketViewSet(viewsets.ModelViewSet):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers
    permission_classes = [IsAuthenticated,IsAdmin]


    #get ticket
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # Admins can see all tickets
            return Ticket.objects.all()
        return Ticket.objects.filter(assigned_to=user)


    #for create a ticket
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #delete response.
    def destroy(self, request, *args, **kwargs):
        
        ticket = self.get_object()
        ticket.delete()
        return Response({'message': 'Ticket deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    #Handle PUT and PATCH requests.
    def update(self, request, *args, **kwargs):
    
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    



