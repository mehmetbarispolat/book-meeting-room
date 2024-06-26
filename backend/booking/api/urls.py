from django.urls import path
from .views import AvailableRooms, BookRoom, AddRoomView, ListRoomsView

urlpatterns = [
    path('availablerooms', AvailableRooms.as_view(), name='available-rooms'),
    path('bookroom', BookRoom.as_view(), name='book-room'),
    path('addroom', AddRoomView.as_view(), name='add_room'),
    path('listrooms', ListRoomsView.as_view(), name='list_rooms'),
]
