# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def anagram(s, t):

    sorted1 = sorted(s)
    sorted2 = sorted(t)

    print(sorted1, sorted2)


    return sorted1 == sorted2

s = "anagram"
t = "nagaram"

print(anagram(s,t))