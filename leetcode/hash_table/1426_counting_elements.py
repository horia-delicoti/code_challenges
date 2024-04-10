# 1426. Counting Elements
# Given an integer array arr, count how many elements x there are,
# such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

# search with array
def countElemenets(arr):
    count = 0

    for x in arr:
        if x+1 in arr:
            count += 1
    
    return count

# search with hashset
def countElements1(arr):
    hash_set = set(arr)
    count = 0

    for x in arr:
        if x+1 in hash_set:
            count += 1
    return count

arr = [1, 2, 3]
arr1 = [1, 3, 2, 3, 5, 0]

print(countElements1(arr1))