import os
import cv2
import numpy as np
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

image_name = '598__M_Left_middle_finger.BMP'
resource_folder = 'FingerSinger\\resources\\SOCOFing\\Real'

image_path = os.path.join(resource_folder, image_name)


def classify_fingerprint(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or unable to load.")

    # Resize image for consistent processing
    image = cv2.resize(image, (128, 128))

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Compute HOG features
    fd, hog_image = hog(blurred, orientations=8, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1), visualize=True, block_norm='L2-Hys')
    
    # Enhance the HOG image for better visualization
    hog_image_rescaled = exposure.rescale_intensity(
        hog_image, in_range=(0, 10))  # type: ignore

    # Simple feature-based classification (example using mean intensity)
    mean_intensity = np.mean(hog_image_rescaled)

    if mean_intensity < 0.2:
        category = "arc"
    elif 0.2 <= mean_intensity < 0.5:
        category = "loop"
    else:
        category = "twirl"
    
    print(f"The fingerprint is classified as: {category} with mean intensity: {mean_intensity}")
    # Visualization
    fig, (ax1, ax2, ax3) = plt.subplots(
        1, 3, figsize=(18, 6), sharex=True, sharey=True)

    ax1.axis('off')
    ax1.imshow(image, cmap=plt.cm.gray_r)
    ax1.set_title('Original Image')

    ax2.axis('off')
    ax2.imshow(blurred, cmap=plt.cm.gray)
    ax2.set_title('Blurred Image')

    ax3.axis('off')
    ax3.imshow(hog_image_rescaled, cmap=plt.cm.gray)
    ax3.set_title('HOG Image')

    plt.show()

    return category, fig

# Example usage


category, fig = classify_fingerprint(image_path)

