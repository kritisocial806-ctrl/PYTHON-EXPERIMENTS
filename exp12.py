def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()
    
    ans = arr[n-1] - arr[0]
    
    small = arr[0] + k
    big = arr[n-1] - k
    
    if small > big:
        small, big = big, small
    
    for i in range(1, n):
        
        if arr[i] - k < 0:
            continue
        
        minimum = min(small, arr[i] - k)
        maximum = max(big, arr[i-1] + k)
        
        ans = min(ans, maximum - minimum)
    
    return ans


# Example
k = 2
arr = [1, 5, 8, 10]
print(getMinDiff(arr, k))   # Output: 5