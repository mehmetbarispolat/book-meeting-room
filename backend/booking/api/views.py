from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    

class AvailableRooms(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        number_of_people = request.query_params.get('number_of_people')
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        
        rooms = Room.objects.all()
        
        if not rooms:
            return Response(status=204)
        
        available_rooms = []
        for room in rooms:
            if not Booking.objects.filter(room=room, end_time__gt=start_time, start_time__lt=end_time).exists():
                available_rooms.append(room)
        serializer = RoomSerializer(available_rooms, many=True)
        return Response({'available_rooms': serializer.data})

class BookRoom(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AddRoomView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ListRoomsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)