import cv2
import numpy as np
threshold1 = 40
threshold2 = 255

#a function that finds the 5 biggest contours
def find_biggest_contours(image, num_contours=5):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply a binary threshold to the image
    _, thresholded = cv2.threshold(image, threshold1, threshold2, cv2.THRESH_BINARY)
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #sort the contours by area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:num_contours]
    return contours

def find_center(image):
    contours = find_biggest_contours(image, 10)
    # Initialize max x and y coordinates
    max_x = max_y = 0
    print(len(contours))
    # Calculate the center of each contour and update max_x and max_y
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:  # to avoid division by zero
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    return (max_x, max_y)

def find_center_avg(image):
    contours = find_biggest_contours(image, 10)
    # Initialize total x and y coordinates
    total_x = total_y = num_contours = 0
    print(len(contours))
    # Calculate the center of each contour and add to total
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:  # to avoid division by zero
            total_x += int(M["m10"] / M["m00"])
            total_y += int(M["m01"] / M["m00"])
            num_contours += 1

    # Calculate the average center of all contours
    if num_contours != 0:  # to avoid division by zero
        center = (total_x // num_contours, total_y // num_contours)
    else:
        center = (0, 0)  # or any default value

    return center

def unwrap_image(image, center, max_radius):
    # The size of the output image
    output_size = (int(360), int(max_radius))  # Width = 360 degrees, Height = max_radius

    # Apply polar to cartesian transformation
    unwrapped_image = cv2.linearPolar(image, center, max_radius, cv2.WARP_FILL_OUTLIERS +  cv2.INTER_LINEAR)

    # Resize to make it easier to view
    # unwrapped_image = cv2.resize(unwrapped_image, output_size, interpolation=cv2.INTER_LINEAR)

    return unwrapped_image

def mouse_callback(event, x, y, flags, param):
    # Check for mouse movement event
    if event == cv2.EVENT_MOUSEMOVE:
        # Display the coordinates on the image window
        coordinates = f"X: {x}, Y: {y}"
        print(coordinates)  # Print coordinates in the console

        
def create_rainbow_gradient(height, width):
    # Create an image filled with zeros (black)
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Calculate the change in color for each step
    for i in range(height):
        hue = int(180 * (i / height))  # Hue goes from 0 to 180 in OpenCV
        hue_color = np.array([[hue, 255, 255]], dtype=np.uint8) # Saturation and Value are always 255
        hue_color = hue_color.reshape(hue_color.shape[0], hue_color.shape[1], 1)  # Ensure hue_color has 3 dimensions
        hue_color = np.repeat(hue_color, 3, axis=2)  # Repeat the single channel to get a 3-channel image
        bgr_color = cv2.cvtColor(hue_color, cv2.COLOR_HSV2BGR) # Convert HSV to RGB
        bgr_color = bgr_color[0, 0, :]  # Reduce bgr_color to a 1D array
        gradient[i, :, :] = bgr_color # Fill each row with the color
    
    return gradient

def apply_gradient_to_edges(image):
    # Create a mask where edges are 1 and non-edges are 0
    mask = image.astype(bool)
    
    # Create the rainbow gradient
    gradient = create_rainbow_gradient(image.shape[0], image.shape[1])
    
    # Apply the mask to the gradient
    rainbow_edges = np.zeros_like(gradient)
    for i in range(3):  # For each color channel
        rainbow_edges[:, :, i] = np.where(mask, gradient[:, :, i], 0)
    
    return rainbow_edges