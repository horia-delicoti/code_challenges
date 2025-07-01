# Given two positive numbers x and y, check if y is a power of x or not.

def power(x, y):
    if x == 1:
        return y == 1
    pow = 1
    while pow < y:
        pow *= x
    return pow == y

x = 10
y = 1

print(power(x, y))

# Time Complexity: O(log y) because we are multiplying x until we reach y.
# Space Complexity: O(1) because we are using a constant amount of space.