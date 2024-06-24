numeros = []
tam = int(input("Quantos valores? "))
for i in range(tam):
    x = int(input())
    numeros.append(x)
numeros.sort()
numeros.reverse()
print(numeros[0])


