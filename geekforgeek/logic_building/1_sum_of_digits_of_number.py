# Given a number n, find the sum of its digits.

def sum_of_digits(n):
    sum = 0

    while n != 0:

        # get last digit
        last = n % 10

        # add last digit to sum
        sum += last

        # remove last digit
        n = n // 10

    return sum

n = 687

print(sum_of_digits(n))

# Time Complexity: O(log n) - The number of digits in n is log n, and we are iterating through each digit.
# Space Complexity: O(1) - We are using a constant amount of space for the sum variable.