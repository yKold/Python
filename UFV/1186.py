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
    if len(lista) != 0:
        media = sum/len(lista) 
    else:
        media = 3247.6
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
count = 0
for i in range(1, 12):
    for j in range(11, 0):
        if count != i:
            lista.append(M[i][j])
            count += 1
            
#   Calculo e resposta
if T == "s" or T == "S":
    res = round(Soma(lista), 1)
    print(f"{res:.1f}")
else:
    res = round(Media(lista), 1)
    print(f"{res:.1f}")

