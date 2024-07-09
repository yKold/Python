lista = [5,3,7,2,63,78,323]
res = []
n = 1

for j in range(0, len(lista)):
    if lista[j] > n:
        n = lista[j]
for i in range(0, n+1):
    for j in lista:
        if i == j:
            res.append(i)
print(res)