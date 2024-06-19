# 643. Maximum Average Subarray

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average
# value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

def findMaxAverage(nums, k):
    window = 0

    for i in range(k):
        window += nums[i]
    
    largest = window

    for right in range(k, len(nums)):
        left = right - k
        window -= nums[left]
        window += nums[right]
        largest = max(largest, window)

    return largest / k


nums = [1,12,-5,-6,50,3]
#nums = [5]
k = 4

print(findMaxAverage(nums, k))
