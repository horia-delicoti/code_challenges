# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums):
    total_sum = 0
    left_sum = 0
    for i in range(len(nums)):
        total_sum += nums[i]
    
    for i in range(len(nums)):
        # Check if left_sum equals right sum
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        left_sum += nums[i]
    return -1
        

nums = [1,7,3,6,5,6]

print(pivotIndex(nums))

# Time Complexity: O(n), where n is the length of the nums array, as we traverse the array twice.
# Space Complexity: O(1), as we are using a constant amount of space for variables