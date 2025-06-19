# You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

def decrement_list(arr):
    for item in range(len(arr)):
        arr[item] -= 1
    return arr

arr = [54, 43, 2, 1, 5]

print(decrement_list(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)
