# Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the answer to each query. A query is true if the sum of
# the subarray from x to y is less than limit, or false otherwise.

# nums = [1, 6, 3, 2, 7, 2]
# queries = [[0, 3], [2, 5], [2, 4]]
# and limit = 13
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def answer_queries(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix) - 1])
    
    return prefix

nums = [3, 6, 2, 8, 1, 4, 1, 5]
print(answer_queries(nums))