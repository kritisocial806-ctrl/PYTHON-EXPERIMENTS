def spiralTraverse(matrix):
    
    result = []
    
    r = len(matrix)
    c = len(matrix[0])
    
    top = 0
    bottom = r - 1
    left = 0
    right = c - 1
    
    while top <= bottom and left <= right:
        
        # Left → Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Top → Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Right → Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Bottom → Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result


# -----------------------
# Driver Code
# -----------------------
if __name__ == "__main__":
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("Spiral Order:", spiralTraverse(matrix))