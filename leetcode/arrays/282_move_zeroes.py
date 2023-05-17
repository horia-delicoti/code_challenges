# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(nums):
    slow = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[slow] == 0:
            nums[slow], nums[i] = nums[i], nums[slow]
        
        if nums[slow] != 0:
            slow += 1



 
#   Time complexity:O(N) Our fast pointer does not visit the same spot twice.

#   Space complexity:O(1) All operations are made in-place
