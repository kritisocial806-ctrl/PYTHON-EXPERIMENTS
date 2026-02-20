def findUnion(a, b):
    union_set = set(a) | set(b)
    return list(union_set)

# Example
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

result = findUnion(a, b)
print("Union:", sorted(result))