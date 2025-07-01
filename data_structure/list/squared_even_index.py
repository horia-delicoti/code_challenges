# Given an Array of integers, return an Array where every element at an even-indexed position is squared. 
#
# Input: array = [9, -2, -9, 11, 56, -12, -3]
# Output: [81, -2, 81, 11, 3136, -12, 9]
# Explanation: The numbers at even indexes (0, 2, 4, 6) have been squared, 
# whereas the numbers at odd indexes (1, 3, 5) have been left the same.

def squareEven(arr):
    # Check for edge cases.
    if arr is None:
        return False

    # Iterate through the original Array
    for i in range(len(arr)):
        # If the index is an even number, then we need to square the element
        if i % 2 == 0:
            arr[i] *= arr[i]
    
    return arr


arr = [9, -2, -9, 11, 56, -12, -3]

print(squareEven(arr))