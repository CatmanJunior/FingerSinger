import cv2
from matplotlib.pylab import f
import numpy as np
import os
from find_core import *
import matplotlib.pyplot as plt

image_name = '1__M_Left_index_finger.BMP'
resource_folder = 'resources\SOCOFing\SOCOFing\Real'

image_path = os.path.join(resource_folder, image_name)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not read the image.")
    exit(1)
    
    
# Gaussian Blur for noise reduction
blurred_image = cv2.GaussianBlur(image, (1, 1), 0)

# Binarization to make the image black and white
_, binary_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)

# Compute the gradient and orientation fields
magnitude, orientation = compute_gradient_orientation(binary_image)
print("Orientation Map:", orientation)
print("Magnitude Map:", magnitude)

# Segment the orientation image into blocks
block_size = 16  # You can adjust the block size
segmented = segment_orientation(orientation, block_size)

poincare_index_map = generate_poincare_index_map(segmented, radius=3)  # Adjust the radius as needed.
print("Poincare Index Map:", poincare_index_map)
core_points_y, core_points_x = find_core_points(poincare_index_map, threshold=0.8)
print("Core points located at:", list(zip(core_points_y, core_points_x)))
# Plot the fingerprint with core points marked
plt.imshow(image, cmap='gray')
for i in range(len(core_points_x)):
    plt.scatter(core_points_x[i], core_points_y[i], c='r', s=100, marker='x')
plt.title("Fingerprint with Core Point(s) Marked")
plt.show()

