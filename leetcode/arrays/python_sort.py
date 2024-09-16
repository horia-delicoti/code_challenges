def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapp = False

        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapp = True

        if swapp == False:
            break
            

arr = [0, 2, 1, 2, 0]

print(bubble_sort(arr))
print(arr)