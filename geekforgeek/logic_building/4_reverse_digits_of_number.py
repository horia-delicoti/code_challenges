# Given an Integer n, find the reverse of its digits.

def reverseNumber(n):
    result = 0

    while (n > 0):
        temp = n % 10
        print("temp : ", temp)
        result = result * 10 + temp
        n = n // 10
    return result


n = 123

print(reverseNumber(n))