# Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case.
# Examples:
# 
# Input: Do geese see God? Output: True
#
# Input: Was it a car or a cat I saw? Output: True
#
#Input: A brown fox jumping over Output: False

def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        while left < right and not string[left].isalnum():
            left += 1
        while left < right and not string[right].isalnum():
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

string = "Do geese see God?"

print(is_palindrome(string))