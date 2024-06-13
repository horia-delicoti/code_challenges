# Find the length of the longest substring of a given string without repeating characters.
#
# Input: abccabcabcc
#
# Output: 3

def longest_substring_without_repeating_characters(string):
    dict = {}

    for value in string:
        if value in dict:
            dict[value] += 1
        else:
            dict[value] = 1

    return len(dict)

input = "abccabcabcc"

print(longest_substring_without_repeating_characters(input))