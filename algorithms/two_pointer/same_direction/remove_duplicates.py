# Given a sorted list of numbers, remove duplicates and return the new length.
# You must do this in-place and without using extra memory.
# 
# Input: [0, 0, 1, 1, 1, 2, 2].
# 
# Output: 3.

def remove_duplicates(arr):
    dict = {}
    result = []

    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for x in dict:
        result.append(x)
    
    return dict



if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2]
    res = remove_duplicates(arr)
    print(res)