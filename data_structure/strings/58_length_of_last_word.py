# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal consisting of non-space characters only.

def lengthOfLastWord(s):
    return len(s.split()[-1]) 

s = "Hello World"
print(lengthOfLastWord(s))

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), where n is the number of words in the string s.