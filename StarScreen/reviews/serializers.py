from rest_framework import serializers


#from app
from .models import Review

#from app movie
from movie.serializers import MovieSerializer
from movie.models import Movie
#from app users
from users.serializers import UserSerializer

#review serializer

#review serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:

        model=Review
        fields = ['id', 'user', 'movie', 'review', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']


    def validate(self, data):

        if not data.get('review'):
            raise serializers.ValidationError("Review is required")
        
        if not data.get('movie'):
            raise serializers.ValidationError("Movie is required")
        
        if not data.get('user'):
            raise serializers.ValidationError("User is required")
        
        return super().validate(data)

    
    #to assign user automaticly
    def create(self,validated_data):

        request=self.context.get('request')
        validated_data['user']=request.user

        return super().create(validated_data)


