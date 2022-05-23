#define pintriger 4
#define pinecho 2

void setup() {
  Serial.begin(9600);
  pinMode(pintriger, OUTPUT);
  pinMode(pinecho, INPUT);
}


void loop() {

  long durasi, jarak;

  digitalWrite(pintriger, LOW);
  delayMicroseconds(2);

  digitalWrite(pintriger, HIGH);
  delayMicroseconds(10);

  digitalWrite(pintriger, LOW);


  durasi = pulseIn(pinecho, HIGH);
  jarak = (durasi / 2) / 29;


  if (jarak >= 200 || jarak <= 0) {
    Serial.println("jarak diluar jangkauan");
  }

  else {

    Serial.print(jarak);

    Serial.println(" cm");

  }

  delay(500);
}