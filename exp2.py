def getMinMax(arr):
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

# Example
arr = [1, 4, 3, 5, 8, 6]

min_val, max_val = getMinMax(arr)

print("Minimum:", min_val)
print("Maximum:", max_val)