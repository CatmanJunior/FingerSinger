
# Fingerprint Analysis

This project is about analyzing and visualizing fingerprints using OpenCV in Python.

## Description

The script takes an image of a fingerprint, applies several image processing techniques to unwrap the fingerprint, and then displays the result. It also calculates and displays the center and average center of the fingerprint.

## Installation 

Install the project dependencies with pip

```bash 
  pip install opencv-python numpy
```
    
## Usage/Examples

To run the script, use the following command:

```bash
  python main.py
```

The script will display a window with the processed fingerprint image. Press any key to close the window.

## Code Explanation

The script performs the following steps:

1. It unwraps the fingerprint and adds a label to the image.
2. It calculates the center and average center of the fingerprint and draws crosses at these points on the image.
3. It converts the image to grayscale and applies a blur and edge detection.
4. It combines the grayscale, blurred, and edge-detected images into a grid and resizes it.
5. It displays the grid image in a window.


