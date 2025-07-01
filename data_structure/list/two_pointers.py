def combine(n, m):
    result = []
    i = j = 0

    while i < len(n) and j < len(m):
        if n[i] < m[j]:
            result.append(n[i])
            i += 1
        else:
            result.append(m[j])
            j += 1
    
    while i < len(n):
        result.append(n[i])
        i += 1
    
    while j < len(m):
        result.append(m[j])
        j += 1


    return result


n = [1, 4, 7, 20]
m = [3, 5, 6]

print(combine(n, m))