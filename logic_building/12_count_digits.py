# Given a natural number n. You have to find the number of digits in it and return it.

def countDigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    print(count)

n = 456

print(countDigits(n))

# Time Complexity: O(log n), where n is the input number. The number of digits in a number is proportional to the logarithm of the number.
# Space Complexity: O(1), as we are using a constant amount of space for the count variable.