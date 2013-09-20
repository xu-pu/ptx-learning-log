//=========================================
// Project 01 -- hello arduino 
// Objective: blink on-board LED on port 13
//==========================================

int ledPin = 13;
int interval = 50;

void setup()
{
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  digitalWrite(ledPin, HIGH);
  delay(interval);
  digitalWrite(ledPin, LOW);
  delay(interval);
}
