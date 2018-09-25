#include <DHT.h>
#include <ESP8266WiFi.h>
#define DHTPIN 4
 
// replace with your channel's thingspeak API key, 
String apiKey = "F4Z3VA8VFPS6XUCF";
const char* ssid = "utkarsh";
const char* password = "utkarsh1";
 
const char* server = "api.thingspeak.com";

int lightPin= A0;  


#define DHTTYPE DHT22 
DHT dht(DHTPIN, DHTTYPE,11);

WiFiClient client;


void setup() {                
  Serial.begin(115200);
  Serial.println("Getting started");
  delay(1000);
  WiFi.begin(ssid, password);
  Serial.println("Begning: ");

  
  dht.begin();
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
   
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
}
 
 
void loop() {   
  float t = dht.readTemperature();
    
  float h = dht.readHumidity();




        int sensorValue=analogRead(lightPin);
        float milliVoltsLight =sensorValue*(5.0/1023.0)*1000;
        float l = milliVoltsLight/10;


          
  if (isnan(h) || isnan(t) || isnan(l)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
 
  if (client.connect(server,80)) {  //   "184.106.153.149" or api.thingspeak.com
    String postStr = apiKey;
           postStr +="&field1=";
           postStr += String((int)t);
           postStr +="&field2=";
           postStr += String((int)l);
           postStr +="&field3=";
           postStr += String((int)h);
 
     client.print("POST /update HTTP/1.1\n"); 
     client.print("Host: api.thingspeak.com\n"); 
     client.print("Connection: close\n"); 
     client.print("X-THINGSPEAKAPIKEY: "+apiKey+"\n"); 
     client.print("Content-Type: application/x-www-form-urlencoded\n"); 
     client.print("Content-Length: "); 
     client.print(postStr.length()); 
     client.print("\n\n"); 
     client.print(postStr);
           
 
     Serial.print("Temperature: ");
     Serial.print(t);
     Serial.print(" degrees Celcius Humidity: "); 
     Serial.print(h);
     Serial.print(" Light intensity: "); 
     Serial.print(l);
     Serial.println("% send to Thingspeak");    
  }
  client.stop();
   
  Serial.println("Waiting...");    
  // time between updates
  delay(2000); // 2 mins
}
