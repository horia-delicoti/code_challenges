# 1832. Check if the sentence is a Pangram
# 
# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters,
# return true if sentence is a pangram, or false otherwise. 


def checkIfPangram(s):
    set1 = (set(s))
    return len(set1) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"

print(checkIfPangram(sentence))
