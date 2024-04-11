from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Room  

class RoomAPITests(APITestCase):

    def setUp(self):
        user = User.objects.create(username="test", password="test")
        self.client.force_authenticate(user=user)
        Room.objects.create(name="Small Conference Room")
        Room.objects.create(name="Large Conference Room")

    def test_get_available_rooms(self):
        url = reverse('available-rooms')
        # params = {'number_of_people': 5, 'start_time': "2023-03-05 09:00:00", "end_time": "2023-03-05 10:00:00"}
        path = f"{url}?number_of_people=5&start_time=2023-03-05 09:00:00&end_time=2023-03-05 10:00:00"
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['available_rooms']), 2)
        self.assertEqual(response.data['available_rooms'], [
            {
                "id": 1,
                "name": "Small Conference Room"
            },
            {
                "id": 2,
                "name": "Large Conference Room"
            }
        ])
        
        
    def test_no_available_rooms(self):
        Room.objects.all().delete()
        url = reverse('available-rooms')
        path = f"{url}?number_of_people=5&start_time=2023-03-05 09:00:00&end_time=2023-03-05 10:00:00"
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_book_room(self):
        url = reverse('book-room')
        data = {
            "room": 1,
            "start_time": "2023-03-05 09:00:00", 
            "end_time": "2023-03-05 10:00:00",
            "number_of_people": 10,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_book_room_wrong_date_format(self):
        url = reverse('book-room')
        data = {
            "room": 1,
            "start_time": "2023-03/05 09:00:00", 
            "end_time": "2023-03-05 10:00:00",
            "number_of_people": 10,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_book_room_start_date_gt_end_date(self):
        url = reverse('book-room')
        data = {
            "room": 1,
            "start_time": "2023-03-05 12:00:00", 
            "end_time": "2023-03-05 10:00:00",
            "number_of_people": 10,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
