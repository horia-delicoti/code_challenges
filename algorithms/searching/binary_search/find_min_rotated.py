# A sorted array of unique integers was rotated at an unknown pivot.
# For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20].
# Find the index of the minimum element in this array.
# Input: [30, 40, 50, 10, 20]
# Output: 3
# Explanation: The smallest element is 10, and its index is 3.
#
# Input: [3, 5, 7, 11, 13, 17, 19, 2]
# Output: 7
# Explanation: The smallest element is 2, and its index is 7.

def find_min_rotated(arr):
    smallest = 0

    for elem in range(1, len(arr)):
        if arr[elem] < arr[smallest]:
            smallest = elem
    return smallest

def find_min_rotated1(arr):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

arr = [3, 5, 7, 11, 13, 17, 19, 2]

print(find_min_rotated(arr))
print(find_min_rotated1(arr))