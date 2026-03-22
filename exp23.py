def minSwaps(arr, k):
    n = len(arr)

    # Step 1: Count elements <= k
    good = 0
    for num in arr:
        if num <= k:
            good += 1

    # Step 2: Count bad elements in first window
    bad = 0
    for i in range(good):
        if arr[i] > k:
            bad += 1

    ans = bad

    # Step 3: Slide window
    i = 0
    j = good

    while j < n:
        if arr[i] > k:
            bad -= 1
        if arr[j] > k:
            bad += 1

        ans = min(ans, bad)

        i += 1
        j += 1

    return ans


# -----------------------
# Driver Code
# -----------------------
if __name__ == "__main__":
    arr = [2, 1, 5, 6, 3]
    k = 3

    print("Minimum Swaps Required:", minSwaps(arr, k))