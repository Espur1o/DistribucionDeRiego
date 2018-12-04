volatile int Pulsos; 
int PinSensor = 2; 
float factor=6.827; 
float volumen=0;
long dt=0; 
long t0=0;

void ContarPulsos ()  
{ 
  Pulsos++;
} 

int ObtenerFrecuencia() 
{
  int frecuencia;
  Pulsos = 0;   
  interrupts();   
  delay(1000);   
  noInterrupts(); 
  frecuencia=Pulsos; //Hz(pulsos por segundo)
  return frecuencia;
}

void setup() 
{ 
  
  Serial.begin(9600); 
  pinMode(PinSensor, INPUT); 
  attachInterrupt(0,ContarPulsos,RISING);
  Serial.println ("Envie 'r' para restablecer el volumen a 0 Litros"); 
  t0=millis();
} 

void loop ()    
{
  if (Serial.available()) {
    if(Serial.read()=='r')volumen=0;
  }
  float frecuencia=ObtenerFrecuencia();
  float caudal_L_m=frecuencia/factor;
  dt=millis()-t0;
  t0=millis();
  volumen=volumen+(caudal_L_m/60)*(dt/1000);

  Serial.print ("Caudal: "); 
  Serial.print (caudal_L_m,3); 
  Serial.print ("L/min");
  Serial.print (" Volumen: "); 
  Serial.print (volumen,3); 
  Serial.println (" L");
}
