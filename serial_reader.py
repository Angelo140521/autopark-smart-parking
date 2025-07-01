import serial
import django
import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autopark.settings")
django.setup()

from parking.models import Sensor

arduino = serial.Serial('COM3', 9600)  # Replace with your port

while True:
    line = arduino.readline().decode('utf-8').strip()
    match = re.match(r"Slot(\d+):(OCCUPIED|AVAILABLE)", line)
    if match:
        slot_num = int(match.group(1))
        status = match.group(2)

        Sensor.objects.update_or_create(
            slot_number=slot_num,
            defaults={'status': status}
        )
        print(f"Updated Slot {slot_num} to {status}")
