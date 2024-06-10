# Given a string original and a string check, find the starting index of
# all substrings of original that is an anagram of check. The output must be sorted in ascending order.
#
# Input: original = "cbaebabacd", check = "abc"
# Output: [0, 6]

def isAnagram(word1, word2):
    return sorted(word1) == word2

def find_all_anagrams(original, check):
    left = 0
    right = len(check)
    res = []
    check = sorted(check)

    while right <= len(original):
        if isAnagram(original[left:right], check):
            res.append(left)
        right += 1
        left += 1

    return res
        

original = "cbaebabacd"
check = "abc"

print(find_all_anagrams(original, check))
