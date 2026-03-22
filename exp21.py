def smallest_subarray(arr, x):
    n = len(arr)
    
    min_length = n + 1
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        # Shrink the window while sum is greater than x
        while current_sum > x:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    if min_length == n + 1:
        return 0
    return min_length


# ---- Driver Code ----
if __name__ == "__main__":
    arr = [1, 4, 45, 6, 0, 19]
    x = 51
    
    result = smallest_subarray(arr, x)
    print("Smallest subarray length:", result)