# You are given an integer n. Your task is to determine whether it is a palindrome.
# A number is considered a palindrome if it reads the same backward as forward, like the string examples "MADAM" or "MOM".

def isPalindrome(n):
    reverse = 0

    temp = abs(n)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    return reverse == abs(n)

n = 1221
print(isPalindrome(n))
