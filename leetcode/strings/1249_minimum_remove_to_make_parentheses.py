# 1249. Minimum remove to make Valid Parentheses
#
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#  Formally, a parentheses string is valid if and only if:
#
#   It is the empty string, contains only lowercase characters, or
#   It can be written as AB (A concatenated with B), where A and B are valid strings, or
#   It can be written as (A), where A is a valid string.

def minRemoveToMakeValid(s):
    stack = []

    # Convert string to list because String is an immutable data structure
    s = list(s)

    for i, char in enumerate(s):

        # Keep track of indices with open parentheses
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = " "
    
    while stack:
        s[stack.pop()] = " "
    return ''.join(s)

s = "lee(t(c)o)de)"

print(minRemoveToMakeValid(s))