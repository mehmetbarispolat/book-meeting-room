from django.urls import path
from .views import AvailableRooms, BookRoom

urlpatterns = [
    path('availablerooms', AvailableRooms.as_view(), name='available-rooms'),
    path('bookroom', BookRoom.as_view(), name='book-room'),
]
