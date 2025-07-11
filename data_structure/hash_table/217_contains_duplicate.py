# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

nums = [1, 2, 3, 1]

print(containsDuplicate(nums))

# Time Complexity: O(n log n) due to sorting and O(n) for the loop
# Space Complexity: O(1) if we ignore the input array, otherwise O(n) for the sorted array