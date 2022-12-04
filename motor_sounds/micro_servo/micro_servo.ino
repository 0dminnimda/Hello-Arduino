#include <Servo.h>

Servo servo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  servo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
//  for (pos = 0; pos <= 180; pos += 3) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
//    servo.write(pos);              // tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15ms for the servo to reach the position
//  }
//  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
//    servo.write(pos);              // tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15ms for the servo to reach the position
//  }
  
  // servo.write(pos);

  for (pos = 0; pos <= 1000; pos += 1){
    servo.write(0);
    delay(10);
  
    servo.write(180);
    delay(10);
  }

//  for (pos = 0; pos <= 180; pos += 1){
//    servo.write(pos);
//    delay(20);
//  }
}
