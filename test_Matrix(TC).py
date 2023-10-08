import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc hình ảnh
# image = cv2.imread('image1.jpg')
# Chuyển thành hình ảnh xám nếu cần
gray_image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)
# Định nghĩa ma trận kernel (3x3 ví dụ)
kernel = np.array([
    [5, 6, 7],
    [8, 9, 10],
    [5, 5, 5]
])

# Kích thước hình ảnh và kernel
image_height, image_width = gray_image.shape
kernel_height, kernel_width = kernel.shape
print(image_height, image_width,"\n",kernel_height, kernel_width )
# Tạo ma trận kết quả (không khởi tạo giá trị ban đầu)
result = np.zeros((image_height - kernel_height + 1, image_width - kernel_width + 1))
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        # Lấy phần ma trận con tương ứng với kernel
        sub_matrix = gray_image[i:i + kernel_height, j:j + kernel_width]
        # Thực hiện phép nhân và tính tổng
        result[i, j] = np.sum(sub_matrix * kernel)
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(gray_image, cmap='gray')
plt.title('Hình ảnh gốc')

plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.title('Hình ảnh sau tích chập')

plt.show()
