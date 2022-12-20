#include <Servo.h>
Servo motor1;
int pot=A0;
char ver;

int ledr=3,ledg=5,ledb=6;


//motor tanımlamaları.
#define l_motor_in1 2
#define l_motor_in2 3
#define l_motor_pwm 9

int ldr=A0;

int trig=13,echo=12;
int zaman,mesafe;

void setup() {
  Serial.begin(9600);
  pinMode(ledr,OUTPUT);
  pinMode(ledg,OUTPUT);
  pinMode(ledb,OUTPUT);
  pinMode(l_motor_in1, OUTPUT);
  pinMode(l_motor_in2, OUTPUT);
  pinMode(l_motor_pwm, OUTPUT);

  pinMode(ledr,OUTPUT);
  pinMode(ledg,OUTPUT);
  pinMode(ledb,OUTPUT);

  motor1.attach(7);
  pinMode(pot,INPUT);

  pinMode(ldr,INPUT);

  pinMode(8,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);

}

void loop() {
if (Serial.available() > 1){
  ver = Serial.read(); 
}
if (ver == 's'){
  for (int i = 0; i < 180; i++){
    motor1.write(i);
    delay(10);
  }

  for (int i = 180; i >= 0; i--){
    motor1.write(i);
    delay(10);
  }
  ver = 'a';
}
if (ver == 'm'){
  motor(100);
}
if (ver == 'd'){
  motor(0);
}
if (ver == 't'){
  motor1.write(0);
}
if (ver == 'r'){
  rgb(true);
}
if (ver == 'o'){
  rgb(false);
}
Serial.print(mesafe_f());
Serial.print(",");
Serial.println(ldr_f());
delay(500);
}

void rgb(bool rgb_durum){
  //ledleri söndür

 if (rgb_durum){
  int deger=random(0,255);
 int deger1=random(0,255);
 int deger2=random(0,255);
  analogWrite(ledr,deger);
  analogWrite(ledg,deger1);
  analogWrite(ledb,deger2);
 }
 else{
 analogWrite(ledr,0);
 analogWrite(ledg,0);
 analogWrite(ledb,0);
 }
}

int mesafe_f(){
  digitalWrite(trig,HIGH);
  delayMicroseconds(100);
  digitalWrite(trig,LOW);
  zaman=pulseIn(echo,HIGH);
  mesafe=(zaman/2)/29.1;
  return mesafe;
}

int ldr_f(){
  int deger3=analogRead(ldr);
  return deger3;
}

void motor(int x){
  digitalWrite(l_motor_in1, 1);
  digitalWrite(l_motor_in2, 0);
  analogWrite(l_motor_pwm, x);
}
