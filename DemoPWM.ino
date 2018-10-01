#include <SoftwareSerial.h>
#include <Servo.h>

Servo s1,s2,s3,s4,s5;
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  s1.attach(3);
  s2.attach(4);
  s3.attach(5);
  s4.attach(6);
  s5.attach(7);
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
}

void loop() { // run over and over
  if (mySerial.available()) {
    String s = mySerial.readStringUntil('!');
    //Serial.println(s);
    String ss1 = s.substring(0,5);
    String ss2 = s.substring(5,10);
    String ss3 = s.substring(10,15);
    String ss4 = s.substring(15,20);
    String ss5 = s.substring(20,25);
    Serial.println(ss1 + ss2 + ss3 + ss4 + ss5);

    int si1 = ss1.toInt();
    int si2 = ss2.toInt();
    int si3 = ss3.toInt();
    int si4 = ss4.toInt();
    int si5 = ss5.toInt();
    s1.write(si1);
    s2.write(si2);
    s3.write(si3);
    s4.write(si4);
    s5.write(si5);
  }
}
