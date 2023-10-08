import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc hình ảnh
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Nhập giá trị cho size (kích thước kernel)
size = 5

# Định nghĩa kernel Gaussian với kích thước size và sigma = 1.0
sigma = 1.0
kernel_size = (size, size)
gaussian_kernel = cv2.getGaussianKernel(size, sigma)
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)

# Kích thước hình ảnh và kernel
image_height, image_width = image.shape
kernel_height, kernel_width = gaussian_kernel.shape

# Tạo ma trận kết quả (không khởi tạo giá trị ban đầu)
result = np.zeros((image_height - kernel_height + 1, image_width - kernel_width + 1), dtype=np.uint8)

# Thực hiện smoothing bằng tích chập
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        sub_matrix = image[i:i + kernel_height, j:j + kernel_width]
        total = np.sum(sub_matrix * gaussian_kernel)
        result[i, j] = np.uint8(total)

# Hiển thị hình ảnh kết quả
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Hình ảnh gốc')

plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.title('Hình ảnh sau tương quan không gian')

plt.show()