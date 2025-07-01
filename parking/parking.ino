#define NUM_SLOTS 4

int trigPins[NUM_SLOTS] = {2, 6, 10, A0};
int echoPins[NUM_SLOTS] = {3, 7, 11, A1};
int greenLEDs[NUM_SLOTS] = {4, 8, 12, A2};
int redLEDs[NUM_SLOTS] = {5, 9, 13, A3};

long duration;
int distance;
int threshold = 10;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < NUM_SLOTS; i++) {
    pinMode(trigPins[i], OUTPUT);
    pinMode(echoPins[i], INPUT);
    pinMode(greenLEDs[i], OUTPUT);
    pinMode(redLEDs[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < NUM_SLOTS; i++) {
    digitalWrite(trigPins[i], LOW);
    delayMicroseconds(2);
    digitalWrite(trigPins[i], HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPins[i], LOW);

    duration = pulseIn(echoPins[i], HIGH);
    distance = duration * 0.034 / 2;

    if (distance < threshold) {
      digitalWrite(redLEDs[i], HIGH);
      digitalWrite(greenLEDs[i], LOW);
      Serial.print("Slot");
      Serial.print(i + 1);
      Serial.println(":OCCUPIED");
    } else {
      digitalWrite(redLEDs[i], LOW);
      digitalWrite(greenLEDs[i], HIGH);
      Serial.print("Slot");
      Serial.print(i + 1);
      Serial.println(":AVAILABLE");
    }
  }
  delay(1000);
}
