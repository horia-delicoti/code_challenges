# A string can be abbreviated by replacing any number of non-adjacent,
# non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

#    "s10n" ("s ubstitutio n")

def valid_abbreviation(word, abbr):
    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0': # Leading zero is not allowed
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if i >= len(word) or word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == len(word) and j == len(abbr)

word = "internationalization"
abbr = "i12iz4n"

print(valid_abbreviation(word, abbr))

# Time Complexity: O(n + m) where n is the length of the word and m is the length of the abbreviation.
# Space Complexity: O(1) because we are using a constant amount of space for the indices and number variable.
