# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(nums):
    n = len(nums)
    dict = {}
    missing = []

    for i in range(n):
        dict[i+1] = 0
    for j in dict:
        dict[nums[j-1]] = 1
    print(dict)

    for x in dict:
        if dict[x] == 0:
            missing.append(x)
    
    return missing
    

nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(nums))

# Time Complexity: O(n) because we traverse the list twice.
# Space Complexity: O(n) for the dictionary used to track the numbers.