# Given an array arr of integers, check if there exist two indices i and j such that :
#
#   i != j
#   0 <= i, j < arr.length
#   arr[i] == 2 * arr[j]


def checkIfExist(arr):
    dict = {}
    for i in range(len(arr)):
        dict[arr[i]] = arr[:i]

    for key,val in dict.items():
        if 2*key in val:
            return True
        elif key%2==0 and key//2 in val:
            return True
        

arr = [10,2, 5,3]

checkIfExist(arr)
