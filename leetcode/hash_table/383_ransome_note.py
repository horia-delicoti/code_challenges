def canConstruct(ransomNote, magazine):
    arr = ""
    for element_ransom in ransomNote:
        for element_magazine in magazine:
            if element_ransom == element_magazine:
                arr += element_ransom
    if arr == ransomNote:
        return 1
    else:
        return 0

ransomNote = "leetcode"
magazine = "arrayodistlec"

canConstruct(ransomNote, magazine)


# Time Complexity O(n*m)