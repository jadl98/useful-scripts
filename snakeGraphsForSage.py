#algoritmo para gráfica recta de n teselas:

# def straightSG(d):
# 	a = {1:[2]}
# 	for i in range(1, d+1):
#         j = 2*i+1
#         a[j] = [j-2,j+1]
#         a[j+1] = [j-1]
#     return a
    	#G = Graph(a)
    	#return G

#algoritmo para grafica zigzag de un numero par d de teselas:
#aprovecha remoción de vértices en sage para crear una con un número impar de teselas

def ZG(d): 

    if d % 2 != 0:
        d=d+1

    nums = [i for i in range(1, 2*d + 2 + 1)]
    print(nums)
    a = {}
    h = 2*d+2
    for j in nums:
        if (j+1) % 4 == 0:
            a[j] = [j+3]
        elif j % 4 == 0:
            a[j] = [j+1]
        else:
            if j+3 <= h:
                a[j] = [j+3, j+1]
    a[h] = [h-1]
    return a

a=ZG(5)
print(a)