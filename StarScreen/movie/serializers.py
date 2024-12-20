#from rest framework
from rest_framework import serializers


#from app
from .models import Movie



class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Movie
        fields='__all__'
        ordering=['created_at']