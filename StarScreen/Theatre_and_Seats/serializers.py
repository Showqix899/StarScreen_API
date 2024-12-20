from rest_framework import serializers
from datetime import date

#model import
from .models import Theatre,Seat,Schedule


#serializer for theatre
class TheatreSerailaers(serializers.ModelSerializer):

    class Meta:
        model=Theatre
        fields=['id','theatre_name','theatre_location','theatre_capacity','screen_types']


#serializer for Seat
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_no', 'theatre', 'row', 'is_available']
        read_only_fields = ['id', 'seat_no', 'row', 'is_available']

    def validate(self, data):
        # Get the theatre ID from the input data
        theatre = data.get('theatre')

        if not theatre:
            raise serializers.ValidationError("Theatre ID is required.")

        # Check if the theatre exists
        try:
            theatre_instance = Theatre.objects.get(id=theatre.id)
        except Theatre.DoesNotExist:
            raise serializers.ValidationError("Theatre with the given ID does not exist.")

        # Check if the theatre has reached its seating capacity
        current_seat_count = Seat.objects.filter(theatre=theatre_instance).count()
        if current_seat_count >= theatre_instance.theatre_capacity:
            raise serializers.ValidationError(f"Theatre '{theatre_instance.theatre_name}' is at full capacity.")

        return data

    def create(self, validated_data):

        theatre = validated_data.get('theatre')

        current_seat_count = Seat.objects.filter(theatre=theatre).count()

        # Define row settings
        row_limit = 50  #Maximum seats per row
        row_initial = "A"  # Starting row letter

        # Calculate the row for the new seat
        row_number = current_seat_count // row_limit
        row_letter = chr(ord(row_initial) + row_number)  # Increment the row letter (A, B, C, etc.)

        # Generate the seat number
        seat_no = f"{row_letter}{(current_seat_count % row_limit) + 1}"

        seat = Seat.objects.create(
            theatre=theatre,
            seat_no=seat_no,
            row=row_letter,
            is_available=True  
        )
        return seat

        
#serializer for Schedule
class ScheduleSerializer(serializers.ModelSerializer):
    
    
    class Meta:

        model=Schedule
        fields=['id','theatre','seat','start_time','end_time','date']
        read_only_fields=['id','theatre','seat']

    
    def validate(self, data):
        
       
        start_time=data.get('start_time')
        end_time=data.get('end_time')

    
        
        if not start_time:
            raise serializers.ValidationError("start_time is required")
        
        if not end_time:
            raise serializers.ValidationError("end_time is required")
        
        if not date:
            raise serializers.ValidationError("date is required")
        
        #start must be before endtime
        if start_time>end_time:
            raise serializers.ValidationError("show start time must be befoe show end time")
        
        if data['date']< date.today():

            raise serializers.ValidationError("Schedule date cannot be in the past.")
        
        # Ensure no overlapping schedules in the same theatre for the same movie 
        overlapping_schedule = Schedule.objects.filter(
            theatre=data['theatre'],
            movie=data['movie'],
            date=data['date'],
            start_time__lt=data['end_time'],  # Start time overlaps
            end_time__gt=data['start_time']   # End time overlaps
        ).exists()


        if overlapping_schedule:
            raise serializers.ValidationError("Overlaping schedule exists for this theatre and movie")
            
         
        return super().validate(data)


    

