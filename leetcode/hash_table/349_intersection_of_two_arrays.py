# Given two integer arrays nums1 and nums2, return an array of their intersection
# Each element in the result must be unique and you may return the result in any order.

def intersection(nums1, nums2):
    result = []
    seen = {}

    for x in nums1:
        seen[x] = 1

    for x in nums2:
        if x in seen and seen[x] == 1:
            result.append(x)
            seen[x] = 0
    
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))
