# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

def reverse_integer(x: int) -> int:
    reverse = 0
    while x != 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
        print(digit)
    return reverse

x = 123
print(reverse_integer(x))