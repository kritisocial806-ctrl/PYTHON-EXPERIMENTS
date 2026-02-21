def isSubset(a, b):
    
    freq = {}
    
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    
    return True


# Example
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

print(isSubset(a, b))   # True