import cv2
import numpy as np

#Đọc ảnh
image = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)

# setting laplacian kernel
laplacian_kernel =   np.array([[-1, -1, -1],
                                  [-1, 8, -1],
                                  [-1, -1, -1]])

# sử dụng filter2D để laplacian ảnh (Convolution)
laplacian = cv2.filter2D(image, -1, laplacian_kernel)
cv2.imwrite('Laplacian filtered image1.jpg', laplacian)

#show ảnh gốc + ảnh laplacian ()
cv2.imshow('Laplacian filtered image', laplacian)
added_image = cv2.add(image, laplacian)
cv2.imwrite('Added image1.jpg', added_image)
# Display the added image
cv2.imshow('Added Image', added_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
