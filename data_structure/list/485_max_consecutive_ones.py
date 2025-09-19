# Given a binary array nums, return the maximum number of consecutive 1's in the array.

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

def findMaxConsecutiveOnesTwoPointer(nums):
    max_count = 0
    slow = 0
        
    for fast in range(len(nums)):
        if nums[fast] == 0:
            # Update max before resetting
            max_count = max(max_count, fast - slow)
            # Move slow to the element after this zero
            slow = fast + 1

    # in case array ends with 1s
    max_count = max(max_count, len(nums)) - slow
    
    return max_count
    


nums = [1, 1, 0, 1, 1 , 1]
findMaxConsecutiveOnesTwoPointer(nums)

# Time Complexity: O(n) because we iterate once the array
# Space Complexity: O(1) because we don't use any extra space