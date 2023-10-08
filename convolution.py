import cv2
import numpy as np

# Đọc hình ảnh từ tệp
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)  # Chắc chắn rằng hình ảnh là ảnh xám

# Định nghĩa kernel
kernel = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

# Sự tương quan không gian
correlation_result = cv2.filter2D(image, -1, kernel)

# Tích chập
convolution_result = cv2.filter2D(image, -1, np.flipud(np.fliplr(kernel)))

# Hiển thị kết quả
cv2.imshow('Correlation Result', correlation_result)
cv2.imshow('Convolution Result', convolution_result)
cv2.waitKey(0)
cv2.destroyAllWindows()