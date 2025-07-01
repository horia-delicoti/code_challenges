# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

def reverseWords(s):
    def reverse(s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1

    s = list(s)
    l = 0
    for right in range(len(s)):
        if s[right] == " ":
            reverse(s, l, right - 1)
            l = right + 1
        elif right == len(s) - 1:
            reverse(s, l, right)
            l = right + 1
    return "".join(s)



s = "Let's take Leetcode contest"

print(reverseWords(s))