# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# 
# Input: nums = [1,2,3,1]
# Output: true

def duplicates(nums):
    hashmap = {}
    
    for i in nums:
        if i in hashmap and hashmap[i] >= 1:
            print("ok")
        hashmap[i] = hashmap.get(i) + 1
    print(hashmap)

    return False
  
        
    


nums = [1, 2, 3, 1]

print(duplicates(nums))