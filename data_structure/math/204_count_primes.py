# Given an integer n, return the number of prime numbers that are strictly less than n.

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def count_primes(n):
    if n <= 2:
        return 0
    
    # Step 1
    is_prime = [True] * n

    # Step 2
    is_prime[0] = is_prime[1] = False

    # Step 3
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False


    return sum(is_prime)

n = 10

print(count_primes(n))