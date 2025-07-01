# Description
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Could you solve it without converting the integer to a string?

def isPalindrome(x: int) -> bool:
    left, right = 0, len(x) - 1

    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome("racecara"))