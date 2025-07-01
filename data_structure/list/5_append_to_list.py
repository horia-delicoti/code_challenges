# You are given three inputs a, b, c. You need to create a list and append a, b, c
# to the list and then return that list.

def append_to_list(a, b ,c):
    result = []

    result.append(a)
    result.append(b)
    result.append(c)

    return result

a = 1
b = 2
c = 3

print(append_to_list(a, b, c))