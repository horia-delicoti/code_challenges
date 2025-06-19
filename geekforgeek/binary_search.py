# Given a sorted array arr and an integer k, find the position(0-based indexing)
# at which k is present in the array using binary search.

# Note: If multiple occurrences are there, please return the smallest index.

def binary_search(arr, k):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        print(f"mid is ", mid)
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return left if [arr[left] == k] else -1

arr = [1, 2, 3, 6, 7]
k = 4

print(binary_search(arr, k))