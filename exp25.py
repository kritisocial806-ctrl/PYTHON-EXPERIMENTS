def findMedian(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# -------------------
# Driver Code
# -------------------
if __name__ == "__main__":
    
    arr1 = [90, 100, 78, 89, 67]
    arr2 = [56, 67, 30, 79]
    arr3 = [1, 2]

    print("Median 1:", findMedian(arr1))
    print("Median 2:", findMedian(arr2))
    print("Median 3:", findMedian(arr3))