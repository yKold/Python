#teste 1
# N = int(input())

# #   pegar valores e juntar o X e Y para tornar 1 só
# for i in range(N):
#     #   mapeia os valores em um Ax... de forma dinamica
#     Ax,Ay,Bx,By,Cx,Cy,Dx,Dy,Rx,Ry = map(int, input().split())

#     #   pegar a posicao do robo para comparar com as posicoes do array
#     posicao_robo = "".join([str(Rx), str(Ry)])
#     valores = set()

#     #   for para pegar cada item de coluna por coluna e linha por linha juntando o X e Y  // verificação para não ter numero negativo no for
#     if Dy - Ay > 0 and Cx - Dx > 0:
#         for j in range( Dy - Ay + 1):
#             for i in range(Cx - Dx + 1):
#                 Y = Ay + j
#                 X = Dx + i 
#                 valores.add("".join([str(X), str(Y)]))
    
#     elif Dy - Ay < 0 and Cx - Dx < 0:
#         for j in range( Ay - Dy + 1):
#             for i in range( Dx - Cx + 1):
#                 Y = Dy + j
#                 X = Cx + i 
#                 valores.add("".join([str(X), str(Y)]))

#     elif Dy - Ay > 0 and Cx - Dx < 0:
#         for j in range( Dy - Ay + 1):
#             for i in range( Dx - Cx + 1):
#                 Y = Ay + j
#                 X = Cx + i 
#                 valores.add("".join([str(X), str(Y)]))

#     elif Dy - Ay < 0 and Cx - Dx > 0:
#         for j in range( Ay - Dy + 1):
#             for i in range( Cx - Dx + 1):
#                 Y = Dy + j
#                 X = Dx + i 
#                 valores.add("".join([str(X), str(Y)]))

#     #   definir resposta como falso para o loop n dar erro
#     res = False
#     #   final dando resposta
#     for i in valores:
#         if i == posicao_robo:
#             res = True
#     if res == True:
#         print("1")
#     else: 
#         print("0")





#teste 2
# N = int(input())

# for _ in range(N):
#     Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = map(int, input().split())

#     min_x = min(Ax, Bx, Cx, Dx)
#     max_x = max(Ax, Bx, Cx, Dx)
#     min_y = min(Ay, By, Cy, Dy)
#     max_y = max(Ay, By, Cy, Dy)

#     if min_x <= Rx <= max_x and min_y <= Ry <= max_y:
#         print("1")
#     else:
#         print("0")





#teste 3
N = int(input())

for _ in range(N):
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = [
        int(x) for x in input().strip().split(' ')]

    print(1 if Ax <= Rx <= Bx and Dx <= Rx <=
          Cx and Ay <= Ry <= Dy and By <= Ry <= Cy else 0)
