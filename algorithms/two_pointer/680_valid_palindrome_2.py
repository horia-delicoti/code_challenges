# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def checkPalindrom(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        right -= 1
        left += 1
    return True

def validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if checkPalindrom(s, left+1, right):
                left += 1
            elif checkPalindrom(s, left, right - 1):
                right -= 1
            else:
                return False
        right -= 1
        left += 1
    return True
        
s = "abccbxa"
print(validPalindrome(s))

# Time Complexity: O(n) because we traverse the string at most twice.
# Space Complexity: O(1) because we use only a constant amount of space.