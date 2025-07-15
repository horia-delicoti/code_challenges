# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    count = 0

    for i in nums:
        if len(str(i)) % 2 == 0:
            count += 1
    return count


nums = [12,345,2,6,7896]

print(findNumbers(nums))

# Time Complexity: O(n) because we iterate once the array
# Space Complexity: O(1) because we don't use any extra space