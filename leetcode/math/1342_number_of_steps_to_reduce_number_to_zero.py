# 1342. Number of Steps to Reduce a Number to Zero
# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
#
# Example 1:
#   Input: num = 14
#   Output: 6
#   Explanation: 
#   Step 1) 14 is even; divide by 2 and obtain 7. 
#   Step 2) 7 is odd; subtract 1 and obtain 6.
#   Step 3) 6 is even; divide by 2 and obtain 3. 
#   Step 4) 3 is odd; subtract 1 and obtain 2. 
#   Step 5) 2 is even; divide by 2 and obtain 1. 
#   Step 6) 1 is odd; subtract 1 and obtain 0.

def numberOfSteps(num):
    step = 0 # We need to keep track of how many steps this takes.
    while num > 0: # Remember, we're taking steps until num is 0.
        if num % 2 == 0: # Modulus operator tells us num is *even*.
            num = num // 2 # So we divide num by 2.
        else: # Otherwise, num must be *odd*.
            num -= 1 # So we subtract 1 from num.
        step += 1 # We *always* increment steps by 1.
    return step # And at the end, the answer is in steps so we return it.

num = 123
print(numberOfSteps(num))