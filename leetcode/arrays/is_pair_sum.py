def isPairSum(A, N, X):

    for i in range(len(A)):
        for j in range(len(A)):

            if A[i] + A[j] == val:
                return i, j
    
    return False

def isPairSum2(A, N, X):
    left = 0
    right = len(A) - 1

    while left < right:
        if A[left] + A[right] == X:
            return left, right
        
        if A[left] + A[right] < X:
            left += 1
        else:
            right -= 1

    return False

arr = [2, 3, 5, 8, 9, 10, 11]
val = 17

print(isPairSum2(arr, len(arr), val))

def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
        
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[i])
        j += 1

    return ans

arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]

print(combine(arr1, arr2))