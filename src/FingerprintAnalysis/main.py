import cv2
import numpy as np
from utils import *
from add_ui import *
import os

image_name = '600__M_Right_index_finger.BMP'
resource_folder = 'FingerSinger\\resources\\SOCOFing\\SOCOFing\\Real'

image_path = os.path.join(resource_folder, image_name)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not read the image.")
    exit(1)

#scale the image
image = cv2.resize(image, (0,0), fx=4, fy=4)

#increase contrast
# image = cv2.convertScaleAbs(image, alpha=2, beta=1)

#convert to 3 channel gray 
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

blur = cv2.GaussianBlur(image, (3,3),5)

# Edge detection 
edges = cv2.Canny(blur, threshold1=15, threshold2=20, apertureSize=3, L2gradient=True)
# edges = cv2.GaussianBlur(edges, (3,3),0)
threshold, contours = find_biggest_contours(blur, 50)

generate_thresholded_images(image)

center = find_center(contours)
center_avg = find_center_avg(contours)

#smooth the edges
edges = cv2.GaussianBlur(edges, (3,3),0)
#apply the gradient to the edges
rainbow_edges = apply_gradient_to_edges(edges)
#unwrap the image
unwrapped = unwrap_image(rainbow_edges, center, 900)

#overlay the contours on the gray image
cv2.drawContours(image, contours, -1, (0, 255, 0), 1)

#add the text center and avgcenter to the image
cv2.putText(image, f'Center: {center}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
cv2.putText(image, f'Avg Center: {center_avg}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

process_images(blur, image, edges, rainbow_edges, unwrapped, center_avg, center)
grid_image = create_grid([blur, image, edges, rainbow_edges, unwrapped])

cv2.imshow('Fingerprint', grid_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
