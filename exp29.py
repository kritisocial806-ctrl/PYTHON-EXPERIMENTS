def rowWithMax1s(arr):
    
    n = len(arr)
    m = len(arr[0])
    
    max_row = -1
    j = m - 1   # Start from top-right
    
    for i in range(n):
        while j >= 0 and arr[i][j] == 1:
            j -= 1
            max_row = i
    
    return max_row


# -----------------------
# Driver Code
# -----------------------

arr1 = [
    [0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]
]

arr2 = [
    [0,0],
    [1,1]
]

arr3 = [
    [0,0],
    [0,0]
]

print("Output 1:", rowWithMax1s(arr1))  # 2
print("Output 2:", rowWithMax1s(arr2))  # 1
print("Output 3:", rowWithMax1s(arr3))  # -1