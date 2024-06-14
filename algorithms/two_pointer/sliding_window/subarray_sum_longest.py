# Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the
# longest subarray that does not exceed 10 is [3, 1, 2, 4],
# so the output is 4 (length of [3, 1, 2, 4]).
#
# Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the 
# longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).

def subarray_sum_longest(nums, target):
    longest, window_sum, left = 0, 0, 0

    for right in range(len(nums)):
        window_sum += nums[right]
    
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
        longest = max(longest, right - left + 1 )
    return longest

nums = [1, 6, 3, 1, 2, 4, 5]
target = 10

print(subarray_sum_longest(nums, target))