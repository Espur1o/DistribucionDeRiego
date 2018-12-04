volatile long Pulsos;
int Sensor=2;

void SumarPulso(){
    Pulsos++;
  }

void setup(){
  Serial.begin(9600);
  pinMode(Sensor, INPUT);
  attachInterrupt(0,SumarPulso,RISING);
  interrupts();
}

void loop(){
  Serial.print("Numero de Pulsos= ");
  Serial.println(Pulsos);
  delay (100);
}
