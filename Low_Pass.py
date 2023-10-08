import cv2
import numpy as np

# Đọc hình ảnh đầu vào
input_image = cv2.imread('image1.jpg')

# Chuyển đổi hình ảnh sang định dạng grayscale (ảnh xám)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc Gaussian để thực hiện lọc thấp
# Thay đổi kernel_size để điều chỉnh độ mờ (độ thấp của bộ lọc)
kernel_size = (5, 5)  # Cỡ của kernel (cửa sổ lọc)
blurred_image = cv2.GaussianBlur(gray_image, kernel_size, 0)

# Áp dụng bộ lọc Laplacian để thực hiện lọc cao
laplacian_image = cv2.Laplacian(gray_image, cv2.CV_64F)

# Chuyển đổi hình ảnh kết quả thành dạng uint8
laplacian_image = np.uint8(np.absolute(laplacian_image))
# Lưu hình ảnh đã lọc thấp
cv2.imwrite('lowpass_filtered_image.jpg', blurred_image)
# Lưu hình ảnh đã lọc cao
cv2.imwrite('highpass_filtered_image.jpg', laplacian_image)
# Hiển thị hình ảnh gốc và hình ảnh đã lọc
cv2.imshow('Original Image', gray_image)
cv2.imshow('Lowpass Filtered Image', blurred_image)
cv2.imshow('Highpass Filtered Image', laplacian_image)

# Đợi đến khi người dùng nhấn phím bất kỳ và sau đó đóng cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()