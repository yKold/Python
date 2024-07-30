# x = 1
# valor = 2
# while x !=0:
#     x = int(input())
#     Matriz = [[0 for i in range(0, x)] for i in range(0, x)]
#     M2 = []
#     for i in range(0, x*x):
#         M2.append(valor**i)
#     for i in range(0, x):
#         for j in range(0, x):
#             Matriz[i][j] = M2[j+i]
#     Ultimo = (len(str(Matriz[x-1][x-1]))) - 1
#     for i in range(0 ,x):
#         print("".join(str(Matriz[i])).replace(",", "").replace("[", "").replace("]", "") )
                
x = 1
valor = 2
while x != 0:
    x = int(input())
    if x == 0:
        break
    
    Matriz = [[0 for i in range(x)] for i in range(x)]
    M2 = []
    for i in range(x * x):
        M2.append(valor**i)
    
    for i in range(x):
        for j in range(x):
            Matriz[i][j] = M2[j + i]
    
    # Determina a largura do campo com base no maior valor da matriz
    max_value = max(max(row) for row in Matriz)
    largura_campo = len(str(max_value))
    
    for i in range(x):
        linha_formatada = " ".join(f"{Matriz[i][j]:{largura_campo}d}" for j in range(x))
        print(linha_formatada)

