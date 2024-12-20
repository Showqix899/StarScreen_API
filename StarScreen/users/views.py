from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator 

# Create your views here.
#rest framework
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError




from .serializers import CustomTokenObtainPairSeralizer,UserSerializer

#from app
from .models import User
from .permissions import IsAdmin
from .utils import generate_verification_token,send_verification_email






#user registration view
class NormalUserRegistrationView(generics.CreateAPIView):

    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

    def perform_create(self,serializer):

        serializer.save(role='user') # assigning the role to user

        # user=serializer.save(role='user',is_verified=False)
        # token = generate_verification_token(user)   # Generate email verification token
        # send_verification_email(user.email,token)  # Send verification email to the user
        

#for admin registration view
class AdminUserRegistrationView(generics.CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class=UserSerializer

    def post(self, request):
        data = request.data
        email = data.get("email")

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user already exists
        try:
            user = User.objects.get(email=email)
            if user.role == "admin":
                return Response({"error": "User with this email is already an admin"}, status=status.HTTP_400_BAD_REQUEST)

            # Update the user's role to admin
            user.role = "admin"
            user.save()
            return Response({"message": "User has been promoted to admin successfully"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            # Create a new admin user if no existing user is found
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save(role='admin') #updating the role
                # serializer.save(role="admin",is_verified=False) # Create admin user and set unverified status
                # token=generate_verification_token(serializer.instance)
                # send_verification_email(data["email",token]) #send verification email
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    






#email verification view
# class VerifyEmailView(APIView):

#     permission_classes=[AllowAny]

#     def get(self,request):

#         token = request.query_params.get('token')  # Get the token from query parameters
#         email = request.query_params.get('email')  # Get the email from query parameters

#         if not token or not email :
#             return Response({"error": "Token and email are required"}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             user=User.objects.get(email=email) #retrive the user by email

#         except User.DoesNotExist:
#             return Response({"error": "Invalid email or token"}, status=status.HTTP_400_BAD_REQUEST)
        
#         if default_token_generator.check_token(user, token): #validate the token

#             user.is_verified=True #mark the user as verified
#             user.save()
#             return Response({"message": "Email verified successfully!"}, status=status.HTTP_200_OK)
        
#         return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
    


    #user login view handle user login view and return jwt tokens (access and refresh token)


 #login view with email verification   
# class LoginView(TokenObtainPairView):

#     serializer_class = CustomTokenObtainPairSeralizer


#     #overiding the post method to include additional data
#     def post(self, request, *args, **kwargs):
#         user = User.objects.filter(email=request.data.get("email")).first()  # Retrieve the user by email
#         if user and not user.is_verified:  # Check if the user is unverified
#             return Response(
#                 {"error": "Email is not verified. Please verify your email first."},
#                 status=status.HTTP_403_FORBIDDEN,
#             )
#         return super().post(request, *args, **kwargs)  # Delegate to parent class if verified


class LoginView(TokenObtainPairView):

    serializer_class=CustomTokenObtainPairSeralizer


    def post(self,request,*args, **kwargs):

        response=super().post(request,*args, **kwargs)

        try:
            #fetch user details based on the provided email
            user=User.objects.get(email=request.data['email'])

            user_data={
                "id":str(user.id),
                "name":user.name,
                "email":user.email,
                "role":user.role,
            }

            #add user details to the response data
            response.data['user']=user_data
        except User.DoesNotExist:  # If no user is found, ensure the response doesn't include invalid user data

            response.data['user']=None

        return response



#user logout view
class LogoutView(APIView):

    def post(self,request,*args, **kwargs):

        try:
            refresh_token=request.data.get("refresh")

            if not refresh_token:

                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            #blacklist the token

            token=RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_205_RESET_CONTENT)
    



