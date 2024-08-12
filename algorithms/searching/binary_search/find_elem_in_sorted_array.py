# Given a sorted array of integers and a target integer, find the first occurrence of the
# target and return its index. Return -1 if the target is not in the array.
#
# Input:
#
#    arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
#    target = 3

def find_first_occurance(arr, target):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        print('mid ', mid)
        print('boundary_index ', boundary_index)
        print('left ', left)
        print('right ', right)

        if arr[mid] == target:
            boundary_index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return boundary_index

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3

print(find_first_occurance(arr, target))