# Linear Search is defined as a sequential search algorithm that
# starts at one end and goes through each element of a list until
# the desired element is found, otherwise the search continues till the end of the data set.

def search(arr, x):
    n = len(arr)

    for i in range(n):
        if x == arr[i]:
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 10

print(search(arr, x))