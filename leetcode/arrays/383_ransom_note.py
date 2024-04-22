# 383. Ransome Note
# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):
    arr = []
    for char_ransom in ransomNote:
        if char_ransom not in magazine:
            return False
        
        location = magazine.index(char_ransom)
        print(location)
        print(char_ransom)

        magazine = magazine[:location] + magazine[location + 1]
    return True


ransomNote = "a"
magazine = "aab"

print(canConstruct(ransomNote, magazine))