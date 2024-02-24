import cv2
import numpy as np


def add_label(image, label):
    coordinates = (10, 30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255) # white color
    thickness = 2
    cv2.putText(image, label, coordinates, font, 1, color, thickness)

def add_cross(image, center, color):
    cross_size = 15
    line_width = 3
    cv2.line(image, (center[0]-cross_size, center[1]), (center[0]+cross_size, center[1]), color, line_width)
    cv2.line(image, (center[0], center[1]-cross_size), (center[0], center[1]+cross_size), color, line_width)

def process_images(blur, gray, edges, rainbow_edges, unwrapped, center_avg, center):
    #overlay the images with names
    add_label(blur, 'Blur')
    add_label(gray, 'Gray')
    add_label(edges, 'Edges')
    add_label(rainbow_edges, 'Rainbow Edges')
    add_label(unwrapped, 'Unwrapped Fingerprint')
    #add a overlay to the gray image of the 2 centers with a cross
    add_cross(gray, center_avg, (255, 0, 255))
    add_cross(gray, center, (0, 255, 255))


def create_grid(img_list, scale=1):
    # Create a grid of images
    #make sure all images have the same amount of color channels
    img_list = [cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) == 2 else img for img in img_list]
    #create a grid
    grid_image = np.concatenate(img_list, axis=1)
    #scale the grid image
    grid_image = cv2.resize(grid_image, (0,0), fx=scale, fy=scale)
    return grid_image

