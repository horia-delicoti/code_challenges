# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.
#
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

def thirdMax(nums):
    # Sort the array
    nums.sort(reverse = True)

    elem_counted = 1
    prev_elem = nums[0]

    for index in range(len(nums)):
    # Current element is different from previous
        if nums[index] != prev_elem:
            elem_counted += 1
            prev_elem = nums[index]
               
    # If we have counted 3 numbers then return current number.
        if elem_counted == 3:
            return nums[index]
       
    # We never counted 3 distinct numbers, return largest number.
    return nums[0]