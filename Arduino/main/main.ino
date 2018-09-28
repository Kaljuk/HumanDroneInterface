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
