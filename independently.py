import cv2
import numpy as np


def zoom_in_with_log_transform(image, factor=2.0):
    """
    Zooms in on an image using a log transformation.

    Parameters:
    - image: Input image (grayscale).
    - factor: Zoom factor. Greater values result in stronger zoom.

    Returns:
    - Zoomed image.
    """
    # Ensure the factor is greater than 1.
    if factor <= 1.0:
        raise ValueError("Zoom factor must be greater than 1.")

    # Apply the log transformation to zoom in.
    zoomed_image = np.log(1 + factor * image)

    # Normalize the image to the range [0, 255].
    zoomed_image = ((zoomed_image - np.min(zoomed_image)) / (np.max(zoomed_image) - np.min(zoomed_image)) * 255).astype(
        np.uint8)

    return zoomed_image


# Load an example grayscale image (you can replace it with your own image).
input_image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Zoom in with a factor of 2.0.
zoomed_image = zoom_in_with_log_transform(input_image, factor=2.0)

# Display the original and zoomed images.
cv2.imshow('Original Image', input_image)
cv2.imshow('Zoomed Image', zoomed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()