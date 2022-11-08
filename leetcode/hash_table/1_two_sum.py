# 1. Two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Brute-force
def sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

# Using hash table
def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic: # This operation is O(1)
            return [i, dic[complement]]
        dic[num] = i
    return [-1, -1]

input = [5, 2, 7, 10, 3, 9]
target = 8

print(twoSum(input, target))