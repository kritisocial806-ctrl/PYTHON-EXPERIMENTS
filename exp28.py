def countLessEqual(row, target):
    left = 0
    right = len(row) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if row[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


def matrixMedian(matrix):
    
    R = len(matrix)
    C = len(matrix[0])
    
    low = matrix[0][0]
    high = matrix[0][C - 1]
    
    for i in range(R):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][C - 1])
    
    desired = (R * C) // 2
    
    while low <= high:
        mid = (low + high) // 2
        
        count = 0
        for i in range(R):
            count += countLessEqual(matrix[i], mid)
        
        if count <= desired:
            low = mid + 1
        else:
            high = mid - 1
    
    return low


# -----------------------
# Driver Code
# -----------------------
if __name__ == "__main__":
    
    mat1 = [
        [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]
    ]
    
    mat2 = [
        [2, 4, 9],
        [3, 6, 7],
        [4, 7, 10]
    ]
    
    mat3 = [[3], [4], [8]]
    
    print("Median 1:", matrixMedian(mat1))
    print("Median 2:", matrixMedian(mat2))
    print("Median 3:", matrixMedian(mat3))