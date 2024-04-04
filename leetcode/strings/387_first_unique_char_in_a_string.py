# 387. First Unique Character in a String
#
# Given a string s, find the first non-repeating character in it and
# return its index. If it does not exist, return -1.
#   Example 1:

#   Input: s = "leetcode"
#   Output: 0

#   Example 2:

#   Input: s = "loveleetcode"
#   Output: 2

#   Example 3:

#   Input: s = "aabb"
#   Output: -1

def firstUniqChar(s):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for x in dict:
        if dict[x] == 1:
            return s.index(x)
    
    return -1

s = "leetcode"
s1 = "loveleetcode"
s2 = "aabb"

print(firstUniqChar(s))