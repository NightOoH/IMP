import cv2
import numpy as np
import matplotlib.pyplot as plt

# Hình ảnh đầu vào (ảnh xám) và kernel (3x3 ví dụ)
gray_image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.array([
    [1, 2, 3],
    [4, 6, 7],
    [7, 8, 9]
])

# Kích thước hình ảnh và kernel
image_height, image_width = len(gray_image), len(gray_image[0])
kernel_height, kernel_width = len(kernel), len(kernel[0])

# Tạo ma trận kết quả (không khởi tạo giá trị ban đầu)
result = [[0 for _ in range(image_width - kernel_width + 1)] for _ in range(image_height - kernel_height + 1)]

# Lật kernel ngược lại
kernel = [row[::-1] for row in kernel]

# Thực hiện tương quan không gian
for i in range(len(result)):
    for j in range(len(result[0])):
        sub_matrix = [row[j:j+kernel_width] for row in gray_image[i:i+kernel_height]]
        result[i][j] = sum(sum(sub_matrix_element * kernel_element for sub_matrix_element, kernel_element in zip(sub_row, kernel_row)) for sub_row, kernel_row in zip(sub_matrix, kernel))

# Hiển thị ma trận kết quả
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(gray_image, cmap='gray')
plt.title('Hình ảnh gốc')

plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.title('Hình ảnh sau tương quan không gian')

plt.show()