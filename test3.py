def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)
    # We need to mask the negative differences
    # since we are looking for values above
    if np.all(mask):
        c = np.abs(diff).argmin()
        return c  # returns min index of the nearest if target is greater than any value
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()


def hist_match(original, specified):
    oldshape = original.shape
    original = original.ravel()
    specified = specified.ravel()

    # get the set of unique pixel values and their corresponding indices and counts
    s_values, bin_idx, s_counts = np.unique(original, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(specified, return_counts=True)

    # Calculate s_k for original image
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]

    # Calculate s_k for specified image
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # Round the values
    sour = np.around(s_quantiles * 255)
    temp = np.around(t_quantiles * 255)

    # Map the rounded values
    b = []
    for data in sour[:]:
        b.append(find_nearest_above(temp, data))
    b = np.array(b, dtype='uint8')

    return b[bin_idx].reshape(oldshape)


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images in greyscale
original = cv2.imread('image1.jpg')
specified = cv2.imread('sang(1).jpg')

# perform Histogram Matching
a = hist_match(original, specified)
result = np.array(a, dtype='uint8')
# Tính toán histogram của hình ảnh gốc và hình ảnh đã cân bằng
hist_original = cv2.calcHist([original], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([result], [0], None, [256], [0, 256])
hist_specified = cv2.calcHist([specified], [0], None, [256], [0, 256])
# Vẽ biểu đồ histogram
plt.figure(figsize=(10, 5))

# Biểu đồ histogram của hình ảnh gốc (màu đen)
plt.plot(hist_original, color='black', label='Hình ảnh gốc')

# Biểu đồ histogram của hình ảnh đã cân bằng (màu đỏ)
plt.plot(hist_equalized, color='red', label='Hình ảnh đã cân bằng')
plt.plot(hist_specified, color='blue', label='Hình ảnh được chỉ định')
# Đặt tiêu đề và nhãn cho biểu đồ
plt.title('So sánh Histogram')
plt.xlabel('Giá trị pixel')
plt.ylabel('Tần suất')

# Display the image
cv2.imshow('result', result)
cv2.imshow('original', original)
cv2.imshow('specified', specified)
plt.legend()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()