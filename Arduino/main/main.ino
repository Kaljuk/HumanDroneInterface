<<<<<<< HEAD
#define PINL 13

void setup() {
  // put your setup code here, to run once:
  
}

void tell(bool on) {
  if (on) digitalWrite(PINL, HIGH);
  else    digitalWrite(PINL, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  tell(true);
  delay(2000);  
  tell(false);
  delay(1000);  
}
=======
/*
 SCP1000 Barometric Pressure Sensor Display

 Shows the output of a Barometric Pressure Sensor on a
 Uses the SPI library. For details on the sensor, see:
 http://www.sparkfun.com/commerce/product_info.php?products_id=8161
 http://www.vti.fi/en/support/obsolete_products/pressure_sensors/

 This sketch adapted from Nathan Seidle's SCP1000 example for PIC:
 http://www.sparkfun.com/datasheets/Sensors/SCP1000-Testing.zip

 Circuit:
 SCP1000 sensor attached to pins 6, 7, 10 - 13:
 DRDY: pin 6
 CSB: pin 7
 MOSI: pin 11
 MISO: pin 12
 SCK: pin 13

 created 31 July 2010
 modified 14 August 2010
 by Tom Igoe
 */

// the sensor communicates using SPI, so include the library:
#include <SPI.h>

//Sensor's memory register addresses:
const int PRESSURE = 0x1F;      //3 most significant bits of pressure
const int PRESSURE_LSB = 0x20;  //16 least significant bits of pressure
const int TEMPERATURE = 0x21;   //16 bit temperature reading
const byte READ = 0b11111100;     // SCP1000's read command
const byte WRITE = 0b00000010;   // SCP1000's write command

// pins used for the connection with the sensor
// the other you need are controlled by the SPI library):
const int dataReadyPin = 6;
const int chipSelectPin = 11;

void setup() {
  Serial.begin(9600);
  SPI.beginTransaction(SPISettings(14000000, MSBFIRST, SPI_MODE0));

  // start the SPI library:
  SPI.begin();

  // initalize the  data ready and chip select pins:
  pinMode(dataReadyPin, INPUT);
  pinMode(chipSelectPin, OUTPUT);

  // give the sensor time to set up:
  delay(100);
}

void loop() {
  Serial.println(SPIRead(0x06));
  
  delay(1000);
}

//Read from or write to register from the SCP1000:

unsigned int SPIRead(byte myRegister) {
  SPI.beginTransaction(SPISettings(4000000, MSBFIRST, SPI_MODE0));
  digitalWrite(chipSelectPin, LOW);
  Serial.println(SPI.transfer(myRegister), BIN);
  delayMicroseconds (20);
  unsigned int result = SPI.transfer(0);
  delayMicroseconds (20);
  digitalWrite(chipSelectPin, HIGH);
  SPI.endTransaction();
  return result;    
}
>>>>>>> f48946d54450b749ab9df4ad2c00391d22ced699
