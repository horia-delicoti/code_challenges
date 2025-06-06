# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        print(f"Checking index {i}, value {nums[i]}")
        for j in range(i + 1, n):
            print(f"Checking index {j}, value {nums[j]}")
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))

# Time Complexity: O(n^2) - The solutions uses a nested loop to check each piar of numbers.
# Space Complexity: 0(1) - Does not use any additional data structures that grow with input size.