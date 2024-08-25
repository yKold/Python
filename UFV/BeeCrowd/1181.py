#   Funções para Somar e calcular Média
def Soma(lista):
    sum = 0
    for i in lista:
        sum+= i
    return sum

def Media(lista):
    sum = 0
    for i in lista:
        sum+= int(i)
    media = sum/len(lista)
    return media

#   Array base com 12x12
M = [[0.0 for i in range(12)] for i in range(12)]

#   Inputs de Linha e se quer Soma ou Média
Linha = int(input())
T = input()

#   Input de todos os valores da matriz
for i in range(12):
    for j in range(12):
        M[i][j] = float(input())

#   Fileira com os valores da LINHA escolhida
lista = [0 for i in range(12)]
for i in range(12):
    lista[i] = M[Linha][i]

#   Calculo e resposta
if T == "s" or T == "S":
    print(Soma(lista))
else:
    print(Media(lista))

