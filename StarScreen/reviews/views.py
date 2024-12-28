from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


#rest framework
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny


#from app
from .serializers import ReviewSerializer
from .models import Review

#from permission
from .permission import IsOwner

#from users permission
from users.permissions import IsAdmin




# Create your views here.

#for posting a review
class ReviewCreateView(CreateAPIView):

    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):

        return {"request":self.request}
    

#for get review
class ReviewListView(APIView):
    permission_classes=[AllowAny]
    
    def get(self, request):

            try:
                movies=Review.objects.all()

                serializer=ReviewSerializer(movies,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except Review.DoesNotExist:
                return Response("The item you loking for is not found")
            

#for Review details
class ReviewDetailsView(APIView):

    permission_classes=[IsAuthenticated]
    def get(self,request,pk):

        try:
            review=get_object_or_404(Review,id=pk)
            serializer=ReviewSerializer(review)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Review.DoesNotExist:
                return Response("The item you loking for is not found")

    


#for update a reviw
class ReviewUpdateView(APIView):

    permission_classes=[IsAuthenticated,IsOwner]

    def put(self,request,pk):

        try:
            review=get_object_or_404(Review,id=pk)
        except Review.DoesNotExist:
            return Response({"message":"Couldn't be found"})
        
        serializer=ReviewSerializer(review,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):

        try:
            review=get_object_or_404(Review,id=pk)
        except Review.DoesNotExist:
            return Response({"message":"Couldn't be Found"})
        
        serializer=ReviewSerializer(review,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    

#for Delete view
class ReviewDeleteView(APIView):

    permission_classes=[IsAuthenticated,IsOwner]

    def delete(self,request,pk):

        try:
            review=get_object_or_404(Review,id=pk)
            review.delete()
            return Response({"message":"successfully deleted"})
        except Review.DoesNotExist:
            return Response({"message":"Couldn't be Found"})
        
        


    




