# You are given an array of integers nums and an integer target.
# Return the number of non-empty subsequences of nums such that the sum of the minimum
# and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

import bisect

def numSubseq(nums, target):
    n = len(nums)
    mod = 10 ** 9 + 7
    nums.sort()

    answer = 0

    for left in range(n):
        right = bisect.bisect_right(nums, target - nums[left]) - 1
        if right >= left:
            answer += pow(2, right - left, mod)
    return answer % mod

nums = [3, 5, 6, 7]
target = 9
print(numSubseq(nums, target))

# Time Complexity: O(n log n) because of sorting and binary search.
# Space Complexity: O(1) for the answer variable and constant space for other variables.
