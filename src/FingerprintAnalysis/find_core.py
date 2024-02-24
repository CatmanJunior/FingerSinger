import cv2
import numpy as np
from typing import Tuple



def compute_gradient_orientation(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # Calculate gradients in x and y directions
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Compute the magnitude and angle of the gradients
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    orientation = np.arctan2(grad_y, grad_x) * (180 / np.pi) % 180
    
    return magnitude, orientation

def segment_orientation(orientation: np.ndarray, block_size: int) -> np.ndarray:
    # Determine the size of the orientation image
    height, width = orientation.shape
    segmented = np.zeros(orientation.shape)
    
    # Iterate over blocks in the orientation image
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            # Calculate the average orientation within this block
            block = orientation[y:y+block_size, x:x+block_size]
            if block.size == 0:
                continue
            avg_orientation = np.mean(block)
            segmented[y:y+block_size, x:x+block_size] = avg_orientation
            
    return segmented

def generate_poincare_index_map(segmented_orientation: np.ndarray, radius: int) -> np.ndarray:
    """Generate a Poincaré index map for a segmented orientation field."""
    height, width = segmented_orientation.shape
    poincare_index_map = np.zeros_like(segmented_orientation)

    for y in range(height):
        for x in range(width):
            poincare_index_map[y, x] = poincare_index_at_point(segmented_orientation, x, y, radius)

    return poincare_index_map

def poincare_index_at_point(segmented_orientation: np.ndarray, x: int, y: int, radius: int) -> float:
    """Calculate the Poincaré Index for a point in a segmented orientation field."""
    angles_around_point = []
    # Define points around the loop L in clockwise direction
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if i == -radius or i == radius or j == -radius or j == radius:
                if 0 <= y+i < segmented_orientation.shape[0] and 0 <= x+j < segmented_orientation.shape[1]:
                    angles_around_point.append(segmented_orientation[y+i, x+j])

    total_change = 0
    for i in range(len(angles_around_point) - 1):
        angle1 = angles_around_point[i]
        angle2 = angles_around_point[(i+1) % len(angles_around_point)]
        total_change += calculate_angle_difference(angle1, angle2)

    # Ensure total angle change is divided by 360 to find index
    poincare_index = total_change / 360.0
    return poincare_index

def find_core_points(poincare_index_map: np.ndarray, threshold: float = 0.8) -> Tuple[np.ndarray, np.ndarray]:
    core_points_y, core_points_x = np.where(poincare_index_map > threshold)
    return core_points_y, core_points_x


def calculate_angle_difference(angle1, angle2):
    """Calculate the minimum difference between two angles."""
    diff = angle2 - angle1
    diff = (diff + 180) % 360 - 180
    return diff

