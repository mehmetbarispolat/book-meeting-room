from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.room.name} booking on {self.start_time.strftime('%Y-%m-%d %H:%M')}"
