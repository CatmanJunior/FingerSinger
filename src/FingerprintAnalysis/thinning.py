import os
import numpy as np
import cv2

def thinning_iteration(im, iter):
# Get the image dimensions
    rows, cols = im.shape
    # Create an empty marker array
    marker = np.zeros((rows, cols), dtype=np.bool_)

    # Define offsets for the 8 neighbors
    neighbors = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    # Iterate over the array (excluding the borders)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            P = [im[i + n[0], j + n[1]] for n in neighbors]
            P0, P1, P2, P3, P4, P5, P6, P7 = P
            C = sum((P[n] == 0 and P[(n + 1) % 8] == 1) for n in range(8)) # Transition count
            N1 = sum(P[n] for n in range(0, 8, 2)) # Neighbors 2, 4, 6, 8
            N2 = sum(P[n] for n in range(1, 8, 2)) # Neighbors 3, 5, 7, 9
            m1 = P0 * P2 * P4 if iter == 0 else P2 * P4 * P6
            m2 = P2 * P4 * P6 if iter == 0 else P0 * P2 * P6
            if im[i, j] == 1 and C == 1 and (N1 >= 2 and N1 <= 3) and m1 == 0 and m2 == 0:
                marker[i, j] = True

    # Convert marker to uint8 for bitwise operation
    marker = marker.astype(np.uint8)
    # Perform the thinning operation
    return im & ~marker

def thinning(im):
    # Normalize the image to binary
    im = (im / 255).astype(np.uint8)
    # Initialize previous image to compare changes
    prev = np.zeros(im.shape, np.uint8)
    # Initialize difference between iterations
    diff = None

    while diff is None or np.sum(diff) > 0:
        im = thinning_iteration(im, 0)
        im = thinning_iteration(im, 1)
        # Calculate difference
        diff = np.abs(im - prev)
        prev = im.copy()
        # cv2.imshow('Thinned Ridges', im * 255)
        # cv2.waitKey(0)
    return im * 255

def apply_ridge_filter(image_path):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Enhance contrast using CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img_enhanced = clahe.apply(img)
    cv2.imshow('Enhanced Image', img_enhanced)
    cv2.waitKey(0)
    # Apply Gaussian Blur to reduce noise
    # img_blur = cv2.GaussianBlur(img_enhanced, (3, 3), 0)
    img_blur = img_enhanced
    # Sobel edge detection to highlight ridges
    # sobelx = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, ksize=3)
    # sobely = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, ksize=3)
    # sobel = np.hypot(sobelx, sobely)
    # cv2.imshow('Sobel Image', sobel)
    # cv2.waitKey(0)
    # Normalize the magnitude to range 0 to 255
    sobel = img_enhanced
    sobel_norm = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)
    
    
    # Convert to uint8
    sobel_image = np.uint8(sobel_norm)

    # Binarize the image
    _, binary_image = cv2.threshold(sobel_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Apply thinning to get single-pixel ridges
    # Assuming thinning() is a function to perform the thinning operation
    thinned_image = thinning(binary_image)  # You need to define or find a suitable thinning function

    return thinned_image

image_name = '567__M_Left_thumb_finger.BMP'
resource_folder = 'resources\SOCOFing\Real'

image_path = os.path.join(resource_folder, image_name)


thinned_ridges = apply_ridge_filter(image_path)
#scale the image to be viewable
thinned_ridges = cv2.resize(thinned_ridges, (0,0), fx=2, fy=2)
cv2.imshow('Thinned Ridges', thinned_ridges)
cv2.waitKey(0)
cv2.destroyAllWindows()