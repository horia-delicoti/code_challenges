# Given an array of integers arr, return true if and only if it is a valid mountain array.
# 
# Input: arr = [0,3,2,1]
# Output: true

def validMountainArray(arr):
    N = len(arr)
    i = 0

    # walk up
    while i+1 < N and arr[i] < arr[i+1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == N-1:
        return False
    
    # walk down
    while i+1 < N and arr[i] > arr[i+1]:
        i += 1
    
    return i == N-1

arr = [0,3,2,1]

print(validMountainArray(arr))