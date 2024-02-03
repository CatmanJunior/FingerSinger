#include <Adafruit_NeoPixel.h>

#define LED_PIN     13
#define LED_COUNT   13
#define PIEZO_COUNT 4
// Define pins for piezo inputs, assuming you're using analog pins A0 to A3
const int piezoPins[PIEZO_COUNT] = {A0, A1, A2, A3};

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show(); // Turn off all pixels ASAP
  // Initialize all piezo pins as input
  for(int i = 0; i < PIEZO_COUNT; i++) {
    pinMode(piezoPins[i], INPUT);
  }
}

void loop() {
  for(int i = 0; i < PIEZO_COUNT; i++) {
    int soundLevel = analogRead(piezoPins[i]);
    // Assuming a threshold for "detecting" a signal. You might need to adjust this.
    if(soundLevel > 100) { // Threshold value, adjust based on your needs
      lightTileInRandomColor(i);
    }
  }
  delay(100); // Small delay to reduce sensitivity and rapid changes
}

void lightTileInRandomColor(int tileNumber) {
  int startLED = tileNumber * 3; // Calculate starting LED for the tile
  uint32_t color = strip.Color(random(0, 255), random(0, 255), random(0, 255));
  
  // Set color for the 3 LEDs in the tile
  for(int i = startLED; i < startLED + 3 && i < LED_COUNT; i++) {
    strip.setPixelColor(i, color);
  }

  strip.show();
}