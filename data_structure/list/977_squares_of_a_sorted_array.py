# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square


    return result
    

input = [-4, -1, 0, 3, 10]
print(sortedSquares(input))
