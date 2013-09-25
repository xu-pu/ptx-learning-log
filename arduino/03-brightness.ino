//==================================================
// Project 03 -- LED brightness
// Objective: use switch to change LED brightness
//==================================================

int switchPin = 8;
int ledPin = 11;
int brightness = 0;
boolean lastState = LOW;

boolean debounce(boolean current) {
  if (current == lastState) {
	  return false;
  }
  else {
    lastState = current;
    return true;
  }
}


void setup() {
  pinMode(switchPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  boolean current = digitalRead(switchPin);
  if ( current == HIGH && debounce(current)) {
    brightness = brightness + 50;
    if (brightness > 255) {
      brightness = 0;
	}
  }			
  analogWrite(ledPin, brightness);
}
