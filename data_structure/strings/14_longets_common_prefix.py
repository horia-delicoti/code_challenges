# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0 : len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))

# Time Complexity: O(S) where S is the sum of all characters in all strings.
# Space Complexity: O(1) because we are not using any extra space.