# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s):
    i = 0
    j = len(s) - 1 

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

s = ["h","e","l","l","o"]

print(reverseString(s))

# Time Complexity: O(n) because we are iterating through half of the array.
# Space Complexity: O(1) because we are not using any extra space.