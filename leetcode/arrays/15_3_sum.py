# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
# that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    # Sort the array to make it easier to avoid duplicates
    nums.sort()
    # Length of the array
    n = len(nums)
    # Result list to store the triplets
    result = []

    # Iterate through each element in the array
    for i in range(n):

        # for each element nums[i], check every
        # other element nums[j] that comes after it
        for j in range(i+1, n):
            # for each pair (nums[i], nums[j]), check every
            # other element nums[k] that comes after it
            # to find a triplet that sums to zero
            for k in range(j+1, n):
                # Check if the sum of the triplet is zero
                if nums[i] + nums[j] + nums[k] == 0:
                    # If it is, append the triplet to the result
                    result.append([nums[i], nums[j], nums[k]])
    # Remove duplicates from the result
    result = [list(x) for x in set(tuple(x) for x in result)]
    # Sort the result to maintain order
    result.sort()
    # Return the result
    return result


nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))

# Time Complexity: O(n^3) because of the three nested loops.
# Space Complexity: O(n) for storing the result.