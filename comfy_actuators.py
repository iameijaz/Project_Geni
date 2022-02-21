# SAMPLE ACTUATOR CODE


const int wheel_index
const int relay1 = 2;
const int relay2 = 3;

#instead of the signals, we are using the buttons for testing the actuaotrs
const int pushButton1=8; 
const int pushButton2=9;


void actuatorPull();
void actuatorPush();
void turnOFF();

void setup() {
 
    pinMode(relay1, OUTPUT);// set pin as output for relay 1
    pinMode(relay2, OUTPUT);// set pin as output for relay 2
    pinMode(pushButton1, INPUT_PULLUP);
    pinMode(pushButton2, INPUT_PULLUP);
    
    // keep the motor off by keeping both HIGH
    digitalWrite(relay1, HIGH); 
    digitalWrite(relay2, HIGH); 

 
  
  Serial.begin(9600);
  delay(2000);
}

void loop() 
{

  while((!(digitalRead(pushButton1)))
  {
   actuatorPull();
  }

  while(!(digitalRead(pushButton2)))
  { 
    actuatorPush();
  }
  
   turnOFF();
          
}
// loop end


void actuatorPush()
{
    digitalWrite(relay1, LOW);// turn relay 1 ON
    digitalWrite(relay2, HIGH);// turn relay 2 OFF  

}

void actuatorPull()
{
   
    digitalWrite(relay1, HIGH);// turn relay 1 OFF
    digitalWrite(relay2, LOW);// turn relay 2 ON
 
}//actuatorPull()


void turnOFF()
{
  
    digitalWrite(relay1, HIGH);// turn relay 1 OFF
    digitalWrite(relay2, HIGH);// turn relay 2 OFF

}