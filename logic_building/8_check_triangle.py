# Given three sides, check whether triangle is valid or not.

def isValidTriangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    return False

a = 8
b = 15
c = 17

print(isValidTriangle(a, b, c))