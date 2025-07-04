# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. The digits are ordered
# from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)  # If all digits were 9, we need to add a new digit
    return digits


digits = [1, 2, 3]
resutl = plusOne(digits)
print(resutl)  # Output: [1, 2, 4]