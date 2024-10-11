# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

def reverseWords(s):
    def reverse(x: list, left: int, right: int):
        while left < right:
            x[left], x[right] = x[right], x[left]
            right -= 1
            left += 1
    
    s = list(s)
    l = 0
    for right in range(len(s)):
        if s[right] == " ":
            reverse(s, l, right)
        elif right == len(s) - 1:
            reverse(s, l, right)
            l = right + 1
    return "".join(s)


s = "Let's take LeetCode contest"

print(reverseWords(s))