import cv2
import numpy as np

def contrast_enhancement_sigmoid(image, alpha=1.0, beta=0.5):
    """
    Tăng cường tương phản của hình ảnh bằng cách áp dụng biến đổi Sigmoid.

    Parameters:
    - image: Hình ảnh đầu vào (grayscale).
    - alpha: Tham số alpha của hàm Sigmoid. Điều này ảnh hưởng đến độ cong của biểu đồ Sigmoid. Giá trị mặc định là 1.0.
    - beta: Tham số beta của hàm Sigmoid. Điều này ảnh hưởng đến vị trí trung tâm của biểu đồ Sigmoid. Giá trị mặc định là 0.5.

    Returns:
    - Hình ảnh sau khi áp dụng biến đổi Sigmoid.
    """
    sigmoid_transformed_image = 1 / (1 + np.exp(-alpha * (image - beta)))
    return sigmoid_transformed_image

# Đọc hình ảnh từ tệp tin (đảm bảo rằng bạn có OpenCV đã được cài đặt).
input_image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng biến đổi Sigmoid với các tham số alpha và beta tùy chọn.
alpha = 0.5
beta = 1
sigmoid_transformed_image = contrast_enhancement_sigmoid(input_image, alpha, beta)

# Hiển thị hình ảnh gốc và hình ảnh sau khi áp dụng biến đổi Sigmoid.
cv2.imshow('Original Image', input_image)
cv2.imshow('Sigmoid Transformed Image', sigmoid_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()