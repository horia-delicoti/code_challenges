#  M     CM         XC      IV
#  1000  100 1000  10 100   1 5
#        900
#        + 1000 - 100

def roman(nums):
    dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    result = 0

    for i in range(len(nums)):
        if i < len(nums) - 1 and dict[nums[i]] < dict[nums[i+1]]:
            result -= dict[nums[i]]
        else:
            result += dict[nums[i]]
    
    return result

s = "MCMXCIV"

print(roman(s))