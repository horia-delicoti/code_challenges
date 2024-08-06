# You should think about binary search anytime the problem provides
# anything sorted. O(log⁡n)O(logn) is extremely fast and binary search
# is usually a huge optimization.

def binarySearch(arr,x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    
    return left


arr = [2, 3, 4, 10, 40]
x = 10

print(binarySearch(arr, x))