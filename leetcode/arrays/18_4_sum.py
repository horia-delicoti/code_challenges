# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
#    0 <= a, b, c, d < n
#    a, b, c, and d are distinct.
#    nums[a] + nums[b] + nums[c] + nums[d] == target


# Time Complexity: O(n^4) because of the four nested loops.
# Space Complexity: O(n) for storing the result.
def fourSum(nums, target):
    # Sort the array to make it easier to avoid duplicates
    nums.sort()
    # Length of the array
    n = len(nums)
    # Result list to store the quadruplets
    result = []

    # Iterate through each element in the array
    for i in range(n):
        # for each element num[i], check other element num[j]
        for j in range(i+1, n):
            # for each pair (nums[i], nums[j]), check every other element nums[k]
            for k in range(j+1, n):
                # for each triplet, check every other element nums[l]
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])

    # Remove duplicates from the result
    result = [list(x) for x in set(tuple(x) for x in result)]
    # Sort the result to maintain order
    result.sort()
    # Return the result
    return result

def fourSum2(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    # trying to use two pointers technique
    for i in range(n):
        for j in range(i+1, n):
            left = j + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums [j] + nums[left] + nums[right]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # Move left and right pointers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

    # Remove duplicates from the result
    result = [list(x) for x in set(tuple(x) for x in result)]
    # Sort the result to maintain order
    result.sort()
    # Return the result
    return result

#nums = [1,0,-1,0,-2,2]
#target = 0
nums = [2,2,2,2,2]
target = 8

print(fourSum2(nums, target))
