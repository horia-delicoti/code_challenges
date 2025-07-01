# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c
# how about c = 2? 
# The answer is True, because 1^2 + 1^2 = 2

import math

def judgeSquareSum(c):
    left, right = 0, int(math.sqrt(c))

    while left <= right:
        sum = left * left + right * right
        if sum == c:
            return True
        elif sum > c:
            right -= 1
        else:
            left += 1
        if left * left == c or right * right == c:
            return True
    return False


c = 5

print(judgeSquareSum(c))

# Time complexity: O(sqrt(c)) because we are iterating from 0 to sqrt(c)
# Space complexity: O(1) because we are using a constant amount of space