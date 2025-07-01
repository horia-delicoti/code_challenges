# 13 Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 }

def romanToInt(string):
    total = 0
    i = 0
    while i < len(string):
        # If this is the subtractive case
        if i + 1 < len(string) and dictionary[string[i]] < dictionary[string[i+1]]:
            total += dictionary[string[i + 1]] - dictionary[string[i]]
            i += 2
        else:
            total += dictionary[string[i]]
            i += 1

    return total

roman = "MMCMLXXXIX"

print(romanToInt(roman))