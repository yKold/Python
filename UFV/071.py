X = int(input())
Y = int(input())
Valores = []
Impares = []
Res = 0

if X > Y:
    Dif = X-Y
    for i in range(Dif-1):
        Valores.append(Y+i+1)
    for i in range(len(Valores)):
        if Valores[i]%2 != 0:
            Impares.append(Valores[i])
    # for i in range(len(Impares)):
    #     Res += Impares[i]
    # Res = sum(Impares)
    # print(Res)
elif X == Y:
    print("0")
else:
    Dif = Y-X
    for i in range(Dif-1):
        Valores.append(X+i+1)
    for i in range(len(Valores)):
        if Valores[i]%2 != 0:
            Impares.append(Valores[i])
    # for i in range(len(Impares)):
    #     Res += Impares[i]
Res = sum(Impares)
print(Res)