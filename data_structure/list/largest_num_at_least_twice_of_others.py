# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much
# as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

def largest_num(nums):
    max_num = max(nums)
    max_index = nums.index(max_num)

    for num in nums:
        if num != max_num and max_num < 2 * num:
            return -1
    return max_index

nums = [3, 6, 1, 0]

print(largest_num(nums))

# Time Complexity: O(n) because we traverse the list a constant number of times.
# Space Complexity: O(1) because we use a constant amount of extra space.
