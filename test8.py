import numpy as np
from scipy.signal import convolve2d
import cv2

# Đọc hình ảnh
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Định nghĩa kernel 1D ngang và kernel 1D dọc
kernel_1d_horizontal = np.array([1, 2, 3])  # Ví dụ kernel Gaussian ngang
kernel_1d_vertical = np.array([1, 2, 3])    # Ví dụ kernel Gaussian dọc

# Thực hiện tích chập 1D ngang và dọc
filtered_image_horizontal = convolve2d(image, kernel_1d_horizontal.reshape(1, -1), mode='same', boundary='wrap')
filtered_image_vertical = convolve2d(filtered_image_horizontal, kernel_1d_vertical.reshape(-1, 1), mode='same', boundary='wrap')

# Chuyển đổi hình ảnh về kiểu dữ liệu 8-bit unsigned integers
filtered_image_horizontal = cv2.convertScaleAbs(filtered_image_horizontal)
filtered_image_vertical = cv2.convertScaleAbs(filtered_image_vertical)

# Kết hợp lại các phần của hình ảnh
combined_image = filtered_image_horizontal + filtered_image_vertical

# Hiển thị hình ảnh kết quả
cv2.imshow("Hình ảnh gốc", image)
cv2.imshow("Hình ảnh kết quả", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()