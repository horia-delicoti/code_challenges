# Recall the same example with input nums = [1, 4, 1, 7, 3, 0, 2, 5] and target = 10,
# then the smallest window with the sum >= 10 is [7, 3] with length 2. So the output is 2.

def subarray_sum_shortest(nums, target):
    window_sum = 0
    left = 0
    shortest = len(nums)

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > target:
            shortest = min(shortest, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return shortest

nums = [1, 4, 1, 7, 3, 0, 2, 5]
target = 10

print(subarray_sum_shortest(nums, target))