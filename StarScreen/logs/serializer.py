from rest_framework import serializers

from .models import Log

class LogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Log
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        