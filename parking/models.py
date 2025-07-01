from django.db import models
from django.contrib.auth.models import User

class Sensor(models.Model):
    slot_number = models.IntegerField(unique=True)
    status = models.CharField(max_length=10)  # 'AVAILABLE', 'OCCUPIED'
    updated_at = models.DateTimeField(auto_now=True)



class ParkingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot_number = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    time_used = models.CharField(max_length=50)
    parking_fee = models.IntegerField()
    reservation_fee = models.IntegerField(default=5)
    total_cost = models.IntegerField()