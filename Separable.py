import numpy as np
from scipy.signal import convolve2d

# Định nghĩa kernel 1D ngang và kernel 1D dọc
kernel_1d_horizontal = np.array([1, 2, 3])  # Ví dụ kernel Gaussian ngang
kernel_1d_vertical = np.array([1, 2, 3])    # Ví dụ kernel Gaussian dọc

# Tạo ma trận hình ảnh ví dụ
image = np.array([[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]])

# Áp dụng tích chập 1D ngang và dọc
filtered_image_horizontal = convolve2d(image, kernel_1d_horizontal.reshape(1, -1), mode='same', boundary='wrap')
filtered_image_vertical = convolve2d(filtered_image_horizontal, kernel_1d_vertical.reshape(-1, 1), mode='same', boundary='wrap')

# In hình ảnh đã lọc
print("Hình ảnh đã lọc (ngang):")
print(filtered_image_horizontal)

print("\nHình ảnh đã lọc (dọc và ngang):")
print(filtered_image_vertical)