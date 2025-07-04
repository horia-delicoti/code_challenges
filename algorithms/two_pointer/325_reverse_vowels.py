# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverseVowels(s):
    left, right = 0, len(s) - 1
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    s = list(s)

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels and s[right] not in vowels:
            right -= 1
        elif s[left] not in vowels and s[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1
    return ''.join(s)

s = "leetcode"
print(reverseVowels(s))

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), for converting the string to a list.
