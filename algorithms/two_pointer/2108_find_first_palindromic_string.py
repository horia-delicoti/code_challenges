# Given an array of strings words, return the first palindromic string in the array.
# If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

def checkPalindrome(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        else:
            right -= 1
            left += 1
    return True


def firstPalindrome(words):
    for word in words:
        if checkPalindrome(word):
            return word
        else:
            return ""

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))

# Time Complexity: O(n * m), where n is the number of words and m is the average length of the words.
# Space Complexity: O(1), since we are using a constant amount of space for the pointers.
