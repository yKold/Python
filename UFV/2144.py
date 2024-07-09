w1 = 1
w2 = 1
r = 1
total = 0
qtd_casos = 0
while w1 or w2 or r != 0:
    entrada = input().split()
    w1 = int(entrada[0])
    w2 = int(entrada[1])
    r = int(entrada[2])
    def contar(w,r):
        return w*(1 + r/30)
    resultado = (contar(w1, r) + contar(w2, r)) / 2
     
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
    total += resultado
    qtd_casos +=1
if total/qtd_casos > 40:
    print("")
    print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")