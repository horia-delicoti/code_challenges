def findMaxConsecutiveOnes(nums):
    max_count = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            print("max_count ", max_count)
            max_count = max(max_count, count)
            print("max_count after = ", max_count)
        else:
            count = 0
            print("count ", count)
    return max_count

nums = [1, 1, 0, 1, 1 , 1]
findMaxConsecutiveOnes(nums)

# Time Complexity: O(n) because we iterate once the array
# Space Complexity: O(1) because we don't use any extra space