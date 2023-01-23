def runningSum(nums):
    # create new array which can be returned as our result
    final_array=[]
    # keep track of current sum
    number=0
    # for every element we encounter in 'nums', add it with current sum and append it to result. 
    for i in nums:
        number += i
        final_array.append(number)
    # return result
    return final_array

nums = [1,2,3,4]
runningSum(nums)