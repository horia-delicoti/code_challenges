# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
# Input: n = 3
# Output: ["1","2","Fizz"]

def fizzBuzz(n):

    # create a list where we add our values
    lista = []

    # iterate from 0 to number
    for i in range(n):
        # Create new iterator because we want to start with 1 and not 0
        j = i + 1

        # If j is divisible by 3 and 5, add to lista "FizzBuzz"
        if j % 3 == 0 and j % 5 == 0:
            lista.append("FizzBuzz")
        # If j is divisible by 3, add to lista "FizzBuzz"
        elif j % 3 == 0:
            lista.append("Fizz")
        # If j is divisible by 5, add to lista "FizzBuzz"
        elif j % 5 == 0:
            lista.append("Buzz")
        else:
        # Default, add to lista the current index converted to String
            lista.append(str(j))
    print(lista)

fizzBuzz(15)

# Time complexity: O(n)  - we have to iterate from one to n and find a value to store for each
# Space complexity: O(1)  - is constant. 