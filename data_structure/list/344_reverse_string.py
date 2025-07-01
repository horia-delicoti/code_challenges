# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverse_string(word):
    left, right = 0, len(word) - 1

    while left < right:
        word[left], word[right] = word[right], word[left]
        left, right = left + 1, right - 1

    return word

word = ["h","e","l","l","o"]
print(reverse_string(word))