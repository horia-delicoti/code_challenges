# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
#
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

def sortArrayByParity(nums):
  slow = 0
  for fast in range(len(nums)):
    if nums[fast] % 2 == 0:
      nums[fast], nums[slow] = nums[slow], nums[fast]
      slow += 1
  return nums

nums = [3, 1, 2, 4]

print(sortArrayByParity(nums))

# Time Complexity: O(n) because we traverse the array once.
# Space Complexity: O(1) because we do not use any extra space.