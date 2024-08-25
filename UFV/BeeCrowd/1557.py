#teste1
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


#teste 2            
# x = 1
# valor = 2
# while x != 0:
#     x = int(input())
#     if x == 0:
#         break
    
#     Matriz = [[0 for i in range(x)] for i in range(x)]
#     M2 = []
#     for i in range(x * x):
#         M2.append(valor**i)
    
#     for i in range(x):
#         for j in range(x):
#             Matriz[i][j] = M2[j + i]
    
#     # Determina a largura do campo com base no maior valor da matriz
#     max_value = max(max(row) for row in Matriz)
#     largura_campo = len(str(max_value))
    
#     for i in range(x):
#         linha_formatada = " ".join(f"{Matriz[i][j]:{largura_campo}d}" for j in range(x))
#         print(linha_formatada)
#     print()



#teste 3
# D = [0]*61
# E = [0]*61

# N = int(input())
# while N >= 0:
#     r=0
#     #preenche os dois vetores com zeros
#     for i in range(61):
#         D[i] = 0
#         E[i] = 0

#     #enquanto tiver botas (N > 0) faça
#     while N:
#         N = N - 1
#         M = int(input())
#         L = input()
        
#         if L=='E':
#             E[M] = E[M] + 1
#         else:
#             D[M] = D[M] + 1

#         if E[M] and D[M]:
#             E[M] = E[M] - 1
#             D[M] = D[M] - 1
#             r = r + 1

#     print(r)
#     N = int(input())





#teste 4
while True:
    try:
        ld = []
        le = []
        pa = 0
        n = int(input())
        for _ in range(n):
            t, l = input().split()
            t = int(t)
            if l == 'D':
                ld.append(t)
            elif l == 'E':
                le.append(t)
        for j in ld:
            if j in le:
                pa += 1
                le.remove(j)
        print(pa)
    except EOFError:
        break