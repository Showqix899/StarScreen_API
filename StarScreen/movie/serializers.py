from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
    

    def validate(self, data):
        # Add any custom logic for fields if needed
        if data['release_date'] > data['expiration']:
            raise serializers.ValidationError("Expiration date must be after release date")
        
        if data['imdb_rating'] < 0 or data['imdb_rating'] > 10:
            raise serializers.ValidationError("IMDB rating must be between 0 and 10")
        
        if data['rotten_tomato'] and (data['rotten_tomato'] < 0 or data['rotten_tomato'] > 100):
            raise serializers.ValidationError("Rotten Tomato rating must be between 0 and 100")
        
        if not data['title']:
            raise serializers.ValidationError("Title is required")
        
        
        

        return super().validate(data)

    def create(self, validated_data):
        # Add any custom logic for fields if needed
        return Movie.objects.create(**validated_data)