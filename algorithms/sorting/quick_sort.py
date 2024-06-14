# QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an
# element as a pivot and partitions the given array around the picked pivot by placing the
# pivot in its correct position in the sorted array.

def partition(array, low, high):
    
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # Traverse through all elements. compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            array[i], array[j] = array[j], array[i]
    
    # swap the pivot element with the greater element specified by i
    array[i+1], array[high] = array[high], array[i+1]

    return i + 1

def quicksort(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pivot - 1)

        # Recursive call on the right of pivot
        quicksort(array, pivot + 1, high)


if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)

    # Function call
    quicksort(array, 0, N - 1)
    print('Sorted array: ')
    for x in array:
        print(x, end=" ")