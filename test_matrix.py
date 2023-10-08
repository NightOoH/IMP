# Định nghĩa ma trận 3x3
matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Định nghĩa ma trận 5x5
matrix_5x5 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Tạo ma trận kết quả 3x3 (kích thước phụ thuộc vào kích thước ma trận gốc và kernel)
result_matrix = []

# Kích thước ma trận kết quả
result_rows = len(matrix_5x5) - len(matrix_3x3) + 1
result_cols = len(matrix_5x5[0]) - len(matrix_3x3[0]) + 1

# Thực hiện tích chập
for i in range(result_rows):
    result_row = []
    for j in range(result_cols):
        sum = 0
        for m in range(len(matrix_3x3)):
            for n in range(len(matrix_3x3[0])):
                sum += matrix_3x3[m][n] * matrix_5x5[i + m][j + n]
        result_row.append(sum)
    result_matrix.append(result_row)
# Thực hiện tích chập và hiển thị tất cả các phép tính
for i in range(result_rows):
    for j in range(result_cols):
        print(f"Phép tính chập tại vị trí [{i}][{j}]:")
        for m in range(len(matrix_3x3)):
            for n in range(len(matrix_3x3[0])):
                product = matrix_3x3[m][n] * matrix_5x5[i + m][j + n]
                print(f"  {matrix_3x3[m][n]} * {matrix_5x5[i + m][j + n]} = {product}")
        print()  # In một dòng trống để phân tách các phép tính
# In ma trận kết quả
for row in result_matrix:
    print(row)
