
#from rest framework
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


#from .models
from .models import User


#user serializer

class UserSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)

    class Meta:

        model=User
        fields = ['id', 'name', 'porfile_pic', 'email', 'phone', 'address', 'dob', 'role', 'password']

    def create(self,validated_data):

        password=validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
    




# class AdminUserSerializer(serializers.ModelSerializer):

#     password=serializers.CharField(write_only=True)

#     class Meta:

#         model=User
#         fields = ['id', 'name', 'porfile_pic', 'email', 'phone', 'address', 'dob', 'role', 'password']

#     def create(self,validated_data):

#         validated_data['role']='admin'
#         password=validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()

#         return user
    


#JWT token serializer

class CustomTokenObtainPairSeralizer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token=super().get_token(user)
        token['role']=user.role
        token['name']=user.name

        return token
    

    


