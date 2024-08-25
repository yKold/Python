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

#   Quer Soma ou Média
T = input()

#   Input de todos os valores da matriz
for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
        # M[i][j] = i

#   Lista para somar ou fazer média
lista = []
for i in range(12):
    for j in range(12):
        if i < j and i != j:
            lista.append(M[i][j])
            
#   Calculo e resposta
if T == "s" or T == "S":
    res = round(Soma(lista)+0.1, 1)
    print(f"{res:.1f}")
else:
    res = round(Media(lista)+0.1, 1)
    print(f"{res:.1f}")

