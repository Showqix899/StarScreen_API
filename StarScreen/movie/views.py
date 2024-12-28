from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404


#from rest framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny


#from app
from .models import Movie
from .serializers import MovieSerializer


#from user app
from users.permissions import IsAdmin

# Create your views here.

#admin Movie Api view
@method_decorator(csrf_exempt, name='dispatch')
class AdminMovieApiView(APIView):

    #checking if the user is admin or not
    permission_classes = [IsAdmin]

    #add a new movie
    def post(self, request):
        data = request.data
        serializer = MovieSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #get all the movie
    def get(self, request):

        try:
            movies=Movie.objects.all()

            serializer=MovieSerializer(movies,many=True)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response("The item you loking for is not found")

    #update a movie instance
    def put(self,request,pk):

        
        movie=get_object_or_404(Movie,id=pk)

        serialiezer=MovieSerializer(movie,request.data)

        if serialiezer.is_valid():
            serialiezer.save()

            return Response(serialiezer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serialiezer.errors)
    
    #to delete a movie
    def delete(self,request,pk):

        try:
            movie=get_object_or_404(Movie,id=pk)
            movie.delete()
            return Response(f'{movie.title} is deleted successfully',status=status.HTTP_200_OK)

        except Movie.DoesNotExist:
           return Response("The item you loking for is not found")
        

    #patch -> for partial update
    def patch(self,request,pk):

        try:
            movie=get_object_or_404(Movie,id=pk)
        except Movie.DoesNotExist:
            return Response({"message":"object not found"},status=status.HTTP_404_NOT_FOUND)
            
        serializer=MovieSerializer(movie,request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#movie list view -> general purpose
class ListOfMovies(APIView):
    
    permission_classes=[AllowAny]
    def get(self,request):

        try:
            movies=Movie.objects.all()

            serializer=MovieSerializer(movies,many=True)
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Movie.DoesNotExist:

            return Response({"message":"couldn't find any"})
    


class MovieDetailsView(APIView):

   

    def get(self,request,id):
        try:
            movie=get_object_or_404(Movie,id=id)

            seralizer=MovieSerializer(movie)

            return Response(seralizer.data,status=status.HTTP_200_OK)
        
        except Movie.DoesNotExist:

            return Response({"message":"couldn't find any"})
            
        
        


        

       
