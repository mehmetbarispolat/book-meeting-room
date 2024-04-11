from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Room, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

class BookingSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        # if Booking.objects.get(room__id=attrs.get("room")).capacity < attrs.get("number_of_people"):
        #     raise serializers.ValidationError("number_of_people must be lower than capacity")
        if attrs.get("start_time") >= attrs.get("end_time"):
            raise serializers.ValidationError("end_time must be greater than start_time")
        return super().validate(attrs)
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time', 'number_of_people']
