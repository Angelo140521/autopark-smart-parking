from rest_framework import serializers
from .models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['slot_number', 'status', 'updated_at']
