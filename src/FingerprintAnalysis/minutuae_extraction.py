import cv2
import numpy as np

def extract_minutiae(thinned_image):
    rows, cols = thinned_image.shape
    minutiae_endings = []
    minutiae_bifurcations = []
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Define 8-neighbors
            P = np.array([
                thinned_image[i-1, j], thinned_image[i-1, j+1], thinned_image[i, j+1],
                thinned_image[i+1, j+1], thinned_image[i+1, j], thinned_image[i+1, j-1],
                thinned_image[i, j-1], thinned_image[i-1, j-1], thinned_image[i-1, j]
            ], dtype=np.uint8)
            
            # Count transitions from 0 to 1
            transitions = np.sum((P[:-1] == 0) & (P[1:] == 1))
            if thinned_image[i, j] == 255:
                # Ridge ending
                if transitions == 1:
                    minutiae_endings.append((j, i))
                # Bifurcation
                elif transitions == 3:
                    minutiae_bifurcations.append((j, i))
    
    return minutiae_endings, minutiae_bifurcations

# Assuming `thinned_image` is the thinned binary image obtained from the previous step
# minutiae_endings, minutiae_bifurcations = extract_minutiae(thinned_image)

# Visualization (Optional, for verification)
# You can visualize the minutiae on the original or enhanced image to verify their correctness.
