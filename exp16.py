def factorial(n):
    fact = 1
    
    for i in range(2, n + 1):
        fact *= i
    
    return list(map(int, str(fact)))


# Example
print(factorial(10))  # Output: [3,6,2,8,8,0,0]