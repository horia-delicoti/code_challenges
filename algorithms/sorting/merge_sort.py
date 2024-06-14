# Merge sort is a recursive algorithm that continuously splits
# the array in half until it cannot be further divided i.e.,
# the array has only one element left (an array with one element is always sorted).
# Then the sorted subarrays are merged into one sorted array.

def mergeSort(arr):
    if len(arr) > 1:
        # finding the mid of the array
        mid = len(arr) // 2

        # dividing the array elements
        L = arr[:mid]
        R = arr[mid:]

        print("L: ", L)
        print("R: ", R)
        
        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is ")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is: ")
    printList(arr)