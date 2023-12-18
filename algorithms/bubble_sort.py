# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the 
# adjacent elements if they are in the wrong order. This algorithm is not suitable for
# large data sets as its average and worst-case time complexity is quite high.


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapp = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapp = True
        if swapp == False:
            break




arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print(arr)