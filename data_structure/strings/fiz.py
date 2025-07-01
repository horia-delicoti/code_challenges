def fizBuzz(n):
    lista = []
    for i in range(n):
        j = i + 1

        if j % 3 == 0 and j % 5 == 0:
            lista.append("FizzBuzz")
        elif j % 3 == 0:
            lista.append("Fizz")
        elif j % 5 == 0:
            lista.append("Buzz")
        else:
            lista.append(j)
    
    return lista

input = 15

print(fizBuzz(input))