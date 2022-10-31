# Description
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Could you solve it without converting the integer to a string?

def isPalindrome(x: int) -> bool:
    # When x < 0, x is not a palindrome
    # If the last digit of the number is 0, to be a palindorme,
    # the first digit of the number also needs to be 0. 
    if (x < 0 or (x != 0 and x % 10 == 0)):
        return False

    reverse_number = 0
    input_number = x

    while (x > 0):
        reverse_number = reverse_number * 10 + x % 10
        x = x // 10
    return reverse_number == input_number

print(isPalindrome(123321))