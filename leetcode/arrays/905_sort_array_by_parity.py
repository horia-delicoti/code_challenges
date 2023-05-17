# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
#
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

def sortArrayByParity(nums):
  i = 0
  j = len(nums) - 1

  while i < j:
    if nums[i] % 2 > nums[j] % 2:
      nums[i], nums[j] = nums[j], nums[i]
    
    if nums[i] % 2 == 0:
      i += 1
    if nums[j] % 2 == 1:
      j -= 1
  
  return nums
