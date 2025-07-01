# Given an array nums of integers and integer k, return the maximum sum such
# that there exists i < j with nums[i] + nums[j] = sum and sum < k.
# If no i, j exist satisfying this equation, return -1.

def two_sum_less_than_k(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    max_sum = -1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < k:
            max_sum = max(max_sum, current_sum)
            left += 1
        else:
            right -= 1
    return max_sum

nums = [34,23,1,24,75,33,54,8]
k = 60

print(two_sum_less_than_k(nums, k))

# Time Complexity: O(n log n) due to sorting, where n is the number of elements in nums.
# Space Complexity: O(1) since we are using a constant amount of extra space.
