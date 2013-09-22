//=========================================
// Project 02 -- hello switch 
// Objective: use switch to control LED
//==========================================

int switchPin = 8;
int ledPin = 13;

void setup() {
  pinMode(switchPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (digitalRead(switchPin) == LOW) {
    digitalWrite(ledPin, HIGH);
  }			
  else {
    digitalWrite(ledPin, LOW);
  }
}
