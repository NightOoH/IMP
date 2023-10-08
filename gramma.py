import cv2
import numpy as np


def adjust_gamma(image, gamma=1.0):
    """
    Adjusts the gamma of an image to enhance or reduce contrast.

    Parameters:
    - image: Input image.
    - gamma: Gamma value. Default is 1.0 (no change).

    Returns:
    - Adjusted image.
    """
    # Ensure gamma is positive.
    if gamma <= 0:
        raise ValueError("Gamma value must be positive.")

    # Apply the gamma correction formula.
    adjusted_image = np.power(image / 255.0, 1.0 / gamma) * 255.0

    # Clip the values to be in the range [0, 255].
    adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)

    return adjusted_image


# Load an example image (you can replace it with your own image).
input_image = cv2.imread('image1.jpg')

# Convert the image to grayscale (optional).
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Adjust gamma to enhance contrast (e.g., increase gamma for more contrast).
adjusted_image1 = adjust_gamma(gray_image, gamma=2.0)
adjusted_image2 = adjust_gamma(gray_image, gamma=3.0)
adjusted_image3 = adjust_gamma(gray_image, gamma=4.0)
# Display the original and adjusted images.
cv2.imshow('Original Image', gray_image)
cv2.imshow('Adjusted Image1', adjusted_image1)
cv2.imshow('Adjusted Image2', adjusted_image2)
cv2.imshow('Adjusted Image3', adjusted_image3)
cv2.waitKey(0)
cv2.destroyAllWindows()