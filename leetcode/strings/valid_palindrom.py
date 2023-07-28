import re

def palindrom(string):
    extracted_string = re.sub('\W+', '', string).lower()
    print(extracted_string)

    left = 0
    right = len(extracted_string) - 1

    while right > left:
        if extracted_string[right] != extracted_string[left]:
            return "Not Palindrom"
        else:
            left += 1
            right -= 1
        
    return "Is Palindrom"

s = "A man, a plan, a canal: Panama"

print(palindrom(s))