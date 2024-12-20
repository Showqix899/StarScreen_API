from rest_framework import serializers




from .models import Ticket



class TicketSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = [
            'id',
            'assigned_to',
            'theatre',
            'seat_no',
            'schedule',
            'movie',
            'created_at',
            'purchased_at',
            'is_booked',
        ]
        read_only_fields = ['id', 'assigned_to', 'theatre', 'seat_no', 'schedule', 'purchased_at']

    def validate(self, data):
        seat = data.get('seat_no')
        theatre = data.get('theatre')
        schedule = data.get('schedule')
        movie = data.get('movie')
        is_booked = data.get('is_booked')

        if not movie:
            raise serializers.ValidationError("this field is requeried")
        if not theatre:
            raise serializers.ValidationError("this field is requeried")
        if not schedule:
            raise serializers.ValidationError("this field is requeried")
        if not seat:
            raise serializers.ValidationError("this field is requeried")

        # Check if the seat is already booked
        if is_booked and seat and seat.is_booked:
            raise serializers.ValidationError("The seat has already been booked.")
        
        # Ensure the seat belongs to the specified theatre
        if seat and seat.theatre != theatre:
            raise serializers.ValidationError("Selected seat does not belong to the specified theatre.")

        # Ensure the seat is available
        if seat and not seat.is_available:
            raise serializers.ValidationError("The selected seat is not available.")

        # Ensure the schedule matches the specified theatre and movie
        if schedule and (schedule.theatre != theatre or schedule.movie != movie):
            raise serializers.ValidationError("Selected schedule does not match the specified theatre and movie.")

        return data

    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not hasattr(request, 'user'):
            raise serializers.ValidationError("Request user is not available.")
        
        # Assign the currently logged-in user to the `assigned_to` field
        validated_data['assigned_to'] = request.user
        
        return super().create(validated_data)
