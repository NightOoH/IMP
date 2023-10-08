import cv2
import numpy as np

# Đọc ảnh đầu vào
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh đã được đọc chưa
if image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng đường dẫn đúng và ảnh tồn tại.")
else:
    # Tách các bit-plane
    bit_planes = [np.bitwise_and(image, 2**i) for i in range(8)]

    # Hiển thị các bit-plane
    for i, bit_plane in enumerate(bit_planes):
        cv2.imshow(f'Bit-Plane {i}', bit_plane * 255)  # Để hiển thị, nhân với 255 để chuyển về ảnh grayscale
        cv2.waitKey(0)

    # Đóng cửa sổ khi bạn nhấn phím bất kỳ
    cv2.destroyAllWindows()