# Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals).
#
#Input: 16
#Output: 4
#Input: 8
#Output: 2
#
#Explanation: square root of 8 is 2.83..., return the integer part

def square_root(n):
    if n == 0:
        return 0
    left, right = 1, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res - 1

n = 16

print(square_root(n))