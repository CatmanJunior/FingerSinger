from picamera import PiCamera
from time import sleep

# Initialize the camera
camera = PiCamera()

# Set camera resolution (optional)
camera.resolution = (1024, 768)

try:
    # Start the camera preview
    camera.start_preview()

    # Wait for 2 seconds to allow the camera to adjust
    sleep(2)

    # Capture an image
    camera.capture('/home/pi/Desktop/image.jpg')

    # Stop the camera preview
    camera.stop_preview()
finally:
    # Ensure the camera is properly closed
    camera.close()