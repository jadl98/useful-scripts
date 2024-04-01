
# de wikipedia, calcula la porción de la n-ésima secuencia de Farey entre 0 y 1 

def farey_sequence(n: int):
    a, b, c, d = 0, 1, 1, n
    #s = [a/b]
    s = [(a,b)]
    while c <= n:
        k = (n + b) // d     #piso de la division
        a, b, c, d = c, d, k * c - a, k * d - b
        s.append((a,b))
    
    return s

