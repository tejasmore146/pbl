#include <LiquidCrystal.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); /// REGISTER SELECT PIN,ENABLE PIN,D4 PIN,D5 PIN, D6 PIN, D7 PIN
char str;
void setup() {
lcd.begin(16,2);
Serial.begin(9600);
}
int i=0;
void loop() {
while(Serial.available())
{
str = Serial.read();
if(str=='*')
{
lcd.setCursor(0, i);
}
else if(str=='-')
{
lcd.clear();
delay(10);
}
else if(str=='#')
{
i=abs(i-1);
}
else if(str=='%')
{
while(str!='!')
{
str=Serial.read();
lcd.scrollDisplayLeft();
delay(1000);
}
}
else
{
lcd.print(str);
delay(200);
}
}
}