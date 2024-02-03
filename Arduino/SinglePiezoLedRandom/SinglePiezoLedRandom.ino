#include <Adafruit_NeoPixel.h>

#define LED_PIN     13
#define LED_COUNT   13
#define MICROPHONE_PIN 2

// Initialize NeoPixel strip.
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();           // Initialize the strip
  strip.show();            // Turn off all pixels ASAP
  pinMode(MICROPHONE_PIN, INPUT);
}

void loop() {
  int soundDetected = digitalRead(MICROPHONE_PIN); // Read the microphone pin

  if (soundDetected == HIGH) {
    lightRandomLedsInSetsOfThree();
    delay(100); // Small delay to debounce and prevent too rapid changes
  }
}

void lightRandomLedsInSetsOfThree() {
  strip.clear(); // Clear all LEDs

  for (int i = 0; i < LED_COUNT; i += 3) {
    // Generate random colors
    uint32_t color = strip.Color(random(0, 255), random(0, 255), random(0, 255));
    
    // Set color for a set of 3 LEDs
    for (int j = i; j < i + 3 && j < LED_COUNT; j++) {
      strip.setPixelColor(j, color);
    }
  }
  
  strip.show(); // Update the strip to show the new colors
}
