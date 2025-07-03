# Given a number n, check if the number is perfect or not. A number is said to be perfect
# if sum of all its factors excluding the number itself is equal to the number.

def isPerfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
# Time complexity: O(n) because we check all numbers from 1 to n-1
# Space complexity: O(1) since we are using a constant amount of space

def isPerfectOptimized(n):
    if n < 2:
        return False
    sum = 1  # Start with 1, as it's a factor of every number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:  # Avoid adding the square root twice
                sum += n // i
    return sum == n
# Time complexity: O(sqrt(n)) because we only check up to the square root of n
# Space complexity: O(1) since we are using a constant amount of space
    

n = 6

print(isPerfect(n))