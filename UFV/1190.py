O = input()
matriz = []
soma1 = 0
soma2 = 0
qnt = 0

for i in range(0,12):
    lista = []
    for j in range(0,12):
        valor = float(input())
        lista.append(valor)
    matriz.append(lista)
    
for i in range(6,12):
    for j in range(i+1,12):
        soma1 += matriz[i][j]
        qnt += 1
        
for i in range(5,0,-1):
    for j in range(7,12):
        if i + j > 11:
            soma2 += matriz[i][j]
            qnt += 1
            
somat = soma1 + soma2
media = somat/qnt

if O == 'S':
    resultado = somat
else:
    resultado = media

print(resultado)