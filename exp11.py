def kthSmallest(arr, k):
    arr.sort()
    return arr[k - 1]


# Example 1
arr1 = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k1 = 4
print("Kth smallest:", kthSmallest(arr1, k1))

# Example 2
arr2 = [7, 10, 4, 3, 20, 15]
k2 = 3
print("Kth smallest:", kthSmallest(arr2, k2))
