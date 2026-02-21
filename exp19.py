def trapWater(arr):
    n = len(arr)
    
    left = 0
    right = n - 1
    
    leftMax = 0
    rightMax = 0
    
    water = 0
    
    while left <= right:
        
        if arr[left] <= arr[right]:
            
            if arr[left] >= leftMax:
                leftMax = arr[left]
            else:
                water += leftMax - arr[left]
            
            left += 1
        
        else:
            
            if arr[right] >= rightMax:
                rightMax = arr[right]
            else:
                water += rightMax - arr[right]
            
            right -= 1
    
    return water


# Example
arr = [3, 0, 1, 0, 4, 0, 2]
print(trapWater(arr))   # Output: 10