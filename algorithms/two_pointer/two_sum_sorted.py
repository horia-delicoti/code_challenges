# Given an array of integers sorted in ascending order, find two numbers that
# add up to a given target. Return the indices of the two numbers in ascending order.
# You can assume elements in the array are unique and there is only one solution.
# Do this in O(n) time and with constant auxiliary space.
#
# Input:
#    arr: a sorted integer array
#    target: the target sum we want to reach
# Input: [2, 3, 4, 5, 8, 11, 18], 8
# Output: 1 3

def two_sum_sorted(arr, target):
    first = 0
    last = len(arr) - 1
    
    while first < last:
        print('first ', arr[first])
        print('last ', arr[last])
        if arr[first] + arr[last] == target:
            return first, last
        elif arr[first] + arr[last] > target:
            last -= 1
        else:
            if arr[first] + arr[last] < target:
                first += 1

arr = [2, 3, 4, 5, 8, 11, 18]
target = 8

print(two_sum_sorted(arr, target))