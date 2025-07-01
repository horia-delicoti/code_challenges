# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
import re

# need to find a way to ignore spaces and special characters
# and check if the string is palindrome or not.
def isPalindrom(string):
    # Remove non-alphanumeric characters and convert to lowercase
    extracted_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()

    left, right = 0, len(extracted_string) - 1
    
    # Two pointer approach to check if the string is palindrome
    while left <= right:
        if extracted_string[left] != extracted_string[right]:
            return False
        else:
            right -= 1
            left += 1
    return True

s = "ab_a"

print(isPalindrom(s))
