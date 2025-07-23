# Given an array arr of integers, check if there exist two indices i and j such that :
# 
#   i != j
#    0 <= i, j < arr.length
#    arr[i] == 2 * arr[j]

def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    return False

arr = [7, 1, 14, 11]

print(checkIfExist(arr))

# Time Complexity: O(n^2) because we are using two nested loops to check each pair of elements.
# Space Complexity: O(1) because we are not using any additional data structures that grow
