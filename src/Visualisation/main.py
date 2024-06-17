import os
import cv2
from matplotlib import pyplot as plt

import numpy as np

# Load the fingerprint image
image_name = 'finger_2.jpg'
resource_folder = 'FingerSinger\\resources'

image_path = os.path.join(resource_folder, image_name)
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Check if the image was successfully loaded
if image is None:
    print("Error: Image not found")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Feature coordinates and labels
    features = {
        'Ridge Ending': (100, 150),
        'Bifurcation': (200, 250),
        'Dot': (300, 350),
        'Short Ridge': (400, 450),
        'Enclosure': (500, 550)
    }

    # Annotations
    for label, (x, y) in features.items():
        # Draw a circle at the feature location
        cv2.circle(image_rgb, (x, y), 5, (255, 0, 0), -1)
        
        # Draw a line to the side of the picture
        line_end_x = x + 100  # Adjust based on your image size
        line_end_y = y
        cv2.line(image_rgb, (x, y), (line_end_x, line_end_y), (0, 255, 0), 2)
        
        # Add a label next to the line
        cv2.putText(image_rgb, label, (line_end_x + 10, line_end_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


# Generate a sine wave
t = np.linspace(0, 1, 500)  # Time from 0 to 1 second, 500 points
frequency = 5  # 5 Hz sine wave as a base
amplitude = 1  # Base amplitude
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)






# Create a figure to hold both the image and the plot
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Annotate for Ridge Ending
plt.annotate('Ridge Ending: Pitch Change', xy=(0.1, 0), xytext=(0.1, -1.2),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10)

# Annotate for Bifurcation
plt.annotate('Bifurcation: Volume Modulation', xy=(0.3, 0.5), xytext=(0.3, 1.5),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10)

# Annotate for Dot (Island)
plt.annotate('Dot: Duration Change', xy=(0.5, 0), xytext=(0.5, -1.2),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10)

# Annotate for Short Ridge
plt.annotate('Short Ridge: Timbre Influence', xy=(0.7, -0.5), xytext=(0.7, -1.5),
             arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=10)

# Annotate for Enclosure (Lake)
plt.annotate('Enclosure: Waveform Shape', xy=(0.9, 0.5), xytext=(0.9, 1.5),
             arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=10)



# Display the fingerprint image
axs[0].imshow(image_rgb)
axs[0].axis('off')  # Hide axis for the image
axs[0].set_title('Fingerprint Features')

# Plot the sine wave on the other subplot
axs[1].plot(t, sine_wave, label='Sine Wave')
axs[1].set_title('Sine Wave Influenced by Fingerprint Features')
axs[1].set_xlabel('Time (seconds)')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show(block=True)