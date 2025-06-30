# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    m = len(needle)
    n = len(haystack)

    for window in range(n - m + 1):
        for i in range(m):
            if needle[i] != haystack[window + i]:
                break
            if i == m - 1:
                return window
    return -1

haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))

# Time Complexity: O(n * m), where n is the length of haystack and m is the length of needle.
# Space Complexity: O(1), since we are using a constant amount of space.