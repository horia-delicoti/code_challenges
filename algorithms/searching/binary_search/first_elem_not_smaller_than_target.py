# Given an array of integers sorted in increasing order and a target, find the index
# of the first element in the array that is larger than or equal to the target.
# Assume that it is guaranteed to find a satisfying number.
#
# Input:
#
#    arr = [1, 3, 3, 5, 8, 8, 10]
#    target = 2

def first_not_smaller(arr, target):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

arr = [2, 3, 5, 7, 11, 13, 17,19]
target = 6

print(first_not_smaller(arr, target))
