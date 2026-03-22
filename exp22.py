def threeWayPartition(arr, a, b):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > b:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1

    return True


# -------------------------
# Driver Code for VS Code
# -------------------------
if __name__ == "__main__":
    arr = [1, 4, 3, 6, 2, 1]
    a = 1
    b = 3

    result = threeWayPartition(arr, a, b)

    print("Modified Array:", arr)
    print("Output:", result)