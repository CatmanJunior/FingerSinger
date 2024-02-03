import cv2
import numpy as np
from utils import apply_gradient_to_edges, find_center_avg, unwrap_image, mouse_callback, find_center
import os

image_name = 'finger_2.jpg'
resource_folder = 'resources'
image_path = os.path.join(resource_folder, image_name)


image = cv2.imread(image_path, cv2.IMREAD_COLOR)

if image is None:
    print("Error: Could not read the image.")
    exit(1)

#increase contrast
# image = cv2.convertScaleAbs(image, alpha=2, beta=1)

#convert to 3 channel gray 
# TODO - This is not the best way to convert to 3 channel
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
center = find_center(gray)
center_avg = find_center_avg(gray)

blur = cv2.GaussianBlur(gray, (15,15),5)

# Edge detection 
edges = cv2.Canny(blur, threshold1=15, threshold2=20, apertureSize=3, L2gradient=True)
#smooth the edges
edges = cv2.GaussianBlur(edges, (3,3),0)
#apply the gradient to the edges
rainbow_edges = apply_gradient_to_edges(edges)
#unwrap the image
unwrapped = unwrap_image(rainbow_edges, center, 900)

#overlay the images with names
cv2.putText(blur, 'Blur', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(gray, 'Gray', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(edges, 'Edges', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(rainbow_edges, 'Rainbow Edges', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(unwrapped, 'Unwrapped Fingerprint', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#add a overlay to the gray image of the 2 centers with a cross
cv2.line(gray, (center_avg[0]-10, center_avg[1]), (center_avg[0]+10, center_avg[1]), (255, 0, 255), 2)
cv2.line(gray, (center_avg[0], center_avg[1]-10), (center_avg[0], center_avg[1]+10), (255, 0, 255), 2)
cv2.line(gray, (center[0]-10, center[1]), (center[0]+10, center[1]), (0, 255, 255), 2)
cv2.line(gray, (center[0], center[1]-10), (center[0], center[1]+10), (0, 255, 255), 2)
#add the text center and avgcenter to the image
cv2.putText(gray, f'Center: {center}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
cv2.putText(gray, f'Avg Center: {center_avg}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

grid_image = np.hstack([ gray, blur, edges, rainbow_edges, unwrapped])

#scale the grid image
grid_image = cv2.resize(grid_image, (0,0), fx=0.4, fy=0.4)

cv2.imshow('Fingerprint', grid_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
