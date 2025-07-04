# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

def uniqueOccurrences(arr):
    dic = {}
    for x in arr:
        dic[x] = arr.count(x)
    
    return len(dic.values()) == len(set(dic.values()))

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))
