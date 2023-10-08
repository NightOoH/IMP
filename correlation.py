import numpy as np

# Định nghĩa một ma trận đầu vào 5x5
matrix = np.array([[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]])

# Định nghĩa một kernel 3x3
kernel = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Sự tương quan không gian
correlation_result = np.zeros((matrix.shape[0] - kernel.shape[0] + 1, matrix.shape[1] - kernel.shape[1] + 1))
for i in range(correlation_result.shape[0]):
    for j in range(correlation_result.shape[1]):
        sub_matrix = matrix[i:i+kernel.shape[0], j:j+kernel.shape[1]]
        correlation_result[i, j] = np.sum(sub_matrix * kernel)

# Tích chập
convolution_result = np.zeros((matrix.shape[0] - kernel.shape[0] + 1, matrix.shape[1] - kernel.shape[1] + 1))
for i in range(convolution_result.shape[0]):
    for j in range(convolution_result.shape[1]):
        sub_matrix = matrix[i:i+kernel.shape[0], j:j+kernel.shape[1]]
        convolution_result[i, j] = np.sum(sub_matrix * np.flipud(np.fliplr(kernel)))

print("Sự tương quan không gian:")
print(correlation_result)
print("\nTích chập:")
print(convolution_result)