# The problem description asks us to do it in place without an extra data structure.
# There are only a couple of things we can do under these constraints - linear traversal or binary search.
#
# if the current element is 0, do nothing
# if the current element is non-0, swap its element with the slow pointer's element and move the slow pointer

def move_zeros(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return arr

arr = [1, 0, 2, 0, 0, 7]
print(move_zeros(arr))
