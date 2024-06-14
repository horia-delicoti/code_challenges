# Selection sort is a simple and efficient sorting algorithm
# that works by repeatedly selecting the smallest (or largest)
# element from the unsorted portion of the list and moving it
# to the sorted portion of the list. 

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # find the min element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]

selection_sort(arr)

print(arr)