import cv2
import numpy as np

# Đọc ảnh gốc
image1 = cv2.imread('image1.jpg')
image = 255-image1
cv2.imwrite('image.jpg', image)
cv2.imshow('image.jpg', image)
cv2.waitKey(0)