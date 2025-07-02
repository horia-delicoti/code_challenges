# Given the number n (n >=0), find its factorial. Factorial of n is defined as 1 x 2 x ... x n.
# For n = 0, factorial is 1. We are going to discuss iterative and recursive programs in this post.

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5

print(factorial_iterative(n))

# Time Complexity: O(n) because we are iterating from 1 to n.
# Space Complexity: O(1) because we are using a constant amount of space for the result variable.