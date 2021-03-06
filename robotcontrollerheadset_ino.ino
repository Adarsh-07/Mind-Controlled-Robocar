#include <IRremote.h>
#include <IRremoteInt.h>
#include <Brain.h>
IRsend irsend;
Brain brain(Serial);
const int ledPin = 3; 
long interval = 500; 
long previousMillis = 0;
int ledState = LOW; 
int medValue;
void setup() {
 // Set up the LED pin.
 pinMode(ledPin, OUTPUT);
 
 // Start the hardware serial.
 Serial.begin(57600);
}
void loop() {
 // Expect packets about once per second.
 if (brain.update()) {
 Serial.println(brain.readCSV());
 
 // Attention runs from 0 to 100.
 medValue = brain.readMeditation();
 }
 
 // Make sure we have a signal.
 if(brain.readSignalQuality() == 0) {
 
 // Send a signal to the LED.
 if (medValue > 65) {
irsend.sendNEC(0xFF10EF, 32); 
 delay(40);
 }
 if (brain.readAttention() > 65) {
irsend.sendNEC(0xFF18E7, 32); 
 delay(40);
 }
 } 
 
}
