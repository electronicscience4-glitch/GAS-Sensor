const int AO_PIN = 26; 
void setup() {
 Serial.begin(115200);
 analogReadResolution(12);  // Set to 12-bit resolution (0-4095) for Pico
 Serial.println("Analog Gas Sensor initialized...");
}
void loop() {
 int gas_value = analogRead(AO_PIN);
 Serial.println(gas_value);
 delay(1000);  // Wait for 1 second
}

