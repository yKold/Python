N = int(input())

for _ in range(N):
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = map(int, input().split())

    posicao_robo = "".join([str(Rx), str(Ry)])
    valores = set()

    # Usar set para armazenar coordenadas e evitar duplicatas
    if Dy - Ay > 0 and Cx - Dx > 0:
        for j in range(Dy - Ay + 1):
            for i in range(Cx - Dx + 1):
                Y = Ay + j
                X = Dx + i
                valores.add("".join([str(X), str(Y)]))

    elif Dy - Ay < 0 and Cx - Dx < 0:
        for j in range(Ay - Dy + 1):
            for i in range(Dx - Cx + 1):
                Y = Dy + j
                X = Cx + i
                valores.add("".join([str(X), str(Y)]))

    elif Dy - Ay > 0 and Cx - Dx < 0:
        for j in range(Dy - Ay + 1):
            for i in range(Dx - Cx + 1):
                Y = Ay + j
                X = Cx + i
                valores.add("".join([str(X), str(Y)]))

    elif Dy - Ay < 0 and Cx - Dx > 0:
        for j in range(Ay - Dy + 1):
            for i in range(Cx - Dx + 1):
                Y = Dy + j
                X = Dx + i
                valores.add("".join([str(X), str(Y)]))

    if posicao_robo in valores:
        print("1")
    else:
        print("0")
