import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc hình ảnh
image = cv2.imread('sang(1).jpg', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem hình ảnh đã được đọc thành công chưa
if image is None:
    print("Không thể đọc hình ảnh. Đảm bảo đường dẫn đến tệp đúng.")
else:
    # Thực hiện cân bằng histogram
    equalized_image = cv2.equalizeHist(image)

    # Hiển thị hình ảnh gốc và hình ảnh đã cân bằng histogram
    plt.figure(figsize=(10, 5))

    plt.subplot(121)
    plt.imshow(image, cmap='gray')
    plt.title('Hình ảnh gốc')
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Hình ảnh đã cân bằng histogram')
    plt.axis('off')

    # Tính toán histogram của hình ảnh gốc và hình ảnh đã cân bằng
    hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    # Vẽ biểu đồ histogram
    plt.figure(figsize=(10, 5))


    # Biểu đồ histogram của hình ảnh gốc (màu đen)
    plt.plot(hist_original, color='black', label='Hình ảnh gốc')

    # Biểu đồ histogram của hình ảnh đã cân bằng (màu đỏ)
    plt.plot(hist_equalized, color='red', label='Hình ảnh đã cân bằng')

    # Đặt tiêu đề và nhãn cho biểu đồ
    plt.title('So sánh Histogram')
    plt.xlabel('Giá trị pixel')
    plt.ylabel('Tần suất')

    # Thêm chú thích cho biểu đồ
    plt.legend()

    plt.show()
    #
    # plt.subplot(121)
    # plt.plot(hist_original, color='black')
    # plt.title('Histogram của hình ảnh gốc')
    # plt.xlabel('Giá trị pixel')
    # plt.ylabel('Tần suất')

    # plt.subplot(122)
    # plt.plot(hist_equalized, color='black')
    # plt.title('Histogram của hình ảnh đã cân bằng')
    # plt.xlabel('Giá trị pixel')
    # plt.ylabel('Tần suất')
