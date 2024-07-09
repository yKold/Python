entrada = input().split()
w1 = int(entrada[0])
w2 = int(entrada[1])
r = int(entrada[2])
def contar(w,r):
    return w*(1 + r/30)
res1 = contar(w1, r)
res2 = contar(w2, r)
resultado = res1 + res2 / 2

if 1<=resultado<13:
    print("Nao vai da nao")
elif 13<=resultado<14:
    print("E 13")
elif 14<=resultado<40:
    print("Bora, hora do show! BIIR!")
elif 40<=resultado<=60:
    print("Ta saindo da jaula o monstro!")
elif resultado>60:
    print("AQUI E BODYBUILDER!!")