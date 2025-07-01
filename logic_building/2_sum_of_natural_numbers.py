# Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i 
    return sum

n = 3
print(sum_of_natural_numbers(n))