# 1133. Largest Unique Number
#
# Given an integer array nums, return the largest integer that only occurs once.
# If no integer occurs once, return -1.
# Example 1:
# 
# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated.
# The number 8 occurs only once, so it is the answer.

def largestUniqueNumber(nums):
    curr_key = 0
    largest_key = -1
    dict = {}

    for num in nums:
        dict[num] = dict.get(num, 0) + 1
    
    for key, value in dict.items():
        if value < 2:
            curr_key = key
            largest_key = max(curr_key, largest_key)
    
    return largest_key


nums = [5,7,3,9,4,9,8,3,1]

print(largestUniqueNumber(nums))