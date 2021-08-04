#define FLAME 2
#define GAS 8

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(FLAME, INPUT);
  pinMode(GAS, INPUT);
}

void loop() {
// put your main code here, to run repeatedly:
  int flame = digitalRead(FLAME);
  int gas = digitalRead(GAS);
  // Digital Read Result : HIGH OR LOW

  if ((flame == HIGH) || (gas == HIGH)) {
//  if (gas == HIGH) {
    Serial.println("PEACE");
  } else {
    Serial.println("WARNING");
  }
  
  delay(500);
}