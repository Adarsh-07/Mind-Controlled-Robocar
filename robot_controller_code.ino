#include <IRremote.h>
int IRpin = 3;
IRrecv irrecv(IRpin);
decode_results results;
int motor_pin1 = 4;
int motor_pin2 = 5;
int motor_pin3 = 6;
int motor_pin4 = 7;

void setup ()
{
  irrecv.enableIRIn();
  pinMode(motor_pin1,OUTPUT);
  pinMode(motor_pin2,OUTPUT);
  pinMode(motor_pin3,OUTPUT);
  pinMode(motor_pin4,OUTPUT);
  Serial.begin(9600);
}

void loop() {
   if (irrecv.decode(&results)) 
    {
         irrecv.resume();   // Receive the next value
    }
  
   if (results.value == 0xFF18E7)  //if gets this code goes forward
     {
       digitalWrite(motor_pin1,LOW);
       digitalWrite(motor_pin2,HIGH);
       digitalWrite(motor_pin3,LOW);
       digitalWrite(motor_pin4,HIGH);
    {
          Serial.println("Go Forward!");
      }
    }
 
   if (irrecv.decode(&results))
{
         irrecv.resume();   // Receive the next value
    }
    if (results.value == 0xFF4AB5)  //if gets this code goes backward
     {
       digitalWrite(motor_pin1,HIGH);
       digitalWrite(motor_pin2,LOW);
       digitalWrite(motor_pin3,HIGH);
       digitalWrite(motor_pin4,LOW);
       {
          Serial.println("Go Backward!");
      }
    }

if (irrecv.decode(&results))
{
         irrecv.resume();   // Receive the next value
    }
    if (results.value == 0xFF10EF)  //if gets this code turns left
     {
        digitalWrite(motor_pin1,HIGH);      
        digitalWrite(motor_pin2,LOW);      
        digitalWrite(motor_pin3,LOW);
        digitalWrite(motor_pin4,HIGH);
        {
          Serial.println("Turn Left!");
      }
    }

if (irrecv.decode(&results))
{
         irrecv.resume();   // Receive the next value
    }
    if (results.value == 0xFF5AA5)  //if gets this code turns right
     {
         digitalWrite(motor_pin1,LOW);       
         digitalWrite(motor_pin2,HIGH);    
         digitalWrite(motor_pin3,HIGH);
         digitalWrite(motor_pin4,LOW);
         {
          Serial.println("Turn Right!");
      }
    }

if (irrecv.decode(&results))
{
         irrecv.resume();   // Receive the next value
    }
    if (results.value == 0xFF38C7)  //if gets this code stops
     {
         digitalWrite(motor_pin1,LOW);       
         digitalWrite(motor_pin2,LOW);    
         digitalWrite(motor_pin3,LOW);
         digitalWrite(motor_pin4,LOW);
         {
          Serial.println("Stop!");
      }
    }
}
