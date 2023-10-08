import cv2
import numpy as np

# Đọc ảnh gốc
image1 = cv2.imread('image1.jpg')

# Tăng độ tương phản bằng cách sử dụng phép nhân
contrast_increase = 1.5  # Giá trị này thể hiện mức độ tăng độ tương phản
contrasted_image = np.clip(image1 * contrast_increase, 0, 255).astype(np.uint8)

# Trừ giá trị pixel ban đầu từ ảnh đã tăng độ tương phản
image2 = contrasted_image - image1

# Lưu ảnh kết quả vào tệp mới
cv2.imwrite('image2.jpg', image2)

# Hiển thị ảnh kết quả (tùy chọn)
cv2.imshow('image2.jpg', image2)
cv2.waitKey(0)

if image1.shape == image2.shape:
    # Thực hiện phép trừ ảnh
    subtracted_image = cv2.subtract(image1, image2)

    # Hiển thị hình ảnh đầu ra (kết quả)
    cv2.imwrite('image3.jpg', subtracted_image)
    cv2.imshow('Subtracted Image', subtracted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Hai hình ảnh không cùng kích thước, không thể thực hiện phép trừ.")