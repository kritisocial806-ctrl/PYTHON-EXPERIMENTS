def find_min_diff(arr, m):
    n = len(arr)

    # If students are more than packets
    if m > n:
        return -1

    # Sort the array
    arr.sort()

    # Initialize minimum difference
    min_diff = float('inf')

    # Find minimum difference among all windows of size m
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


# ---- Driver Code ----
if __name__ == "__main__":
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5
    result = find_min_diff(arr, m)
    print("Minimum difference:", result)