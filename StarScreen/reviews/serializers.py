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
    movie = MovieSerializer(read_only=True)  # Nested movie details for the response

    class Meta:

        model=Review
        fields = ['id', 'user', 'movie', 'review', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']


    # #custom de serialization
    # def validate(self, attrs):
        
    #     request = self.context.get('request')  # Get request context
    #     movie_id = self.initial_data.get('movie')  # Fetch movie ID from raw input data

    #     if not movie_id:
    #         raise serializers.ValidationError({"movie": "This field is required."})

    #     try:
    #         attrs['movie'] = Movie.objects.get(id=movie_id)
    #     except Movie.DoesNotExist:
    #         raise serializers.ValidationError({"movie": "Invalid movie ID."})

    #     attrs['user'] = request.user  # Attach the authenticated user to the validated data
    #     return attrs


    
    #to assign user automaticly
    def create(self,validated_data):

        request=self.context.get('request')
        validated_data['user']=request.user

        return super().create(validated_data)


