from math import floor
RES = []
RES_C = []
SOBRA = 0
SOBRA_C = 0
VALOR = float(input())
Cents = VALOR- floor(VALOR) 

# Inicio Notas
Val = VALOR
if VALOR % 100 == 0:
    RES.append(VALOR/100)
else:
    RES.append(VALOR/100)
    SOBRA = VALOR % 100
    if SOBRA % 50 == 0:
        RES.append(SOBRA/50)
    else:
        RES.append(SOBRA/50)
        SOBRA = SOBRA%50
        if SOBRA % 20 == 0:
            RES.append(SOBRA/20)
        else:
            RES.append(SOBRA/20)
            SOBRA = SOBRA%20
            if SOBRA % 10 == 0:
                RES.append(SOBRA/10)
            else:
                RES.append(SOBRA/10)
                SOBRA = SOBRA%10
                if SOBRA % 5 == 0:
                    RES.append(SOBRA/5)
                else:
                    RES.append(SOBRA/5)
                    SOBRA = SOBRA%5
                    if SOBRA % 2 == 0:
                        RES.append(SOBRA/2)
                    else:
                        RES.append(SOBRA/2)
                        SOBRA = SOBRA%2
                        if SOBRA % 1 == 0:
                            RES.append(1)
                        else: 
                            RES.append(SOBRA/1)
                            SOBRA = SOBRA%1
RES.append(0)
RES.append(0)

V100 = int(RES[0])
V50 = int(RES[1])
V20 = int(RES[2])
V10 = int(RES[3])
V5 = int(RES[4])
V2 = int(RES[5])
V1 = int(RES[6])

print("NOTAS:")
print("{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00".format(V100, V50, V20, V10, V5, V2))

# Inicio Centavos
Cents *= 100
Cents = int(Cents)

if Cents !=0:
    if Cents % 100 == 0:
        RES_C.append(Cents/100)
    else:
        RES_C.append(Cents/100)
        SOBRA_C = Cents % 100
        if SOBRA_C % 50 == 0:
            RES_C.append(SOBRA_C/50)
        else:
            RES_C.append(SOBRA_C/50)
            SOBRA_C = SOBRA_C%50
            if SOBRA_C % 25 == 0:
                RES_C.append(SOBRA_C/25)
            else:
                RES_C.append(SOBRA_C/25)
                SOBRA_C = SOBRA_C%25
                if SOBRA_C % 10 == 0:
                    RES_C.append(SOBRA_C/10)
                else:
                    RES_C.append(SOBRA_C/10)
                    SOBRA_C = SOBRA_C%10
                    if SOBRA_C % 5 == 0:
                        RES_C.append(SOBRA_C/5)
                    else:
                        RES_C.append(SOBRA_C/5)
                        SOBRA_C = SOBRA_C%5
                        if SOBRA_C % 1 == 0:
                            RES_C.append(SOBRA_C/1)
                        else:
                            RES_C.append(SOBRA_C/1)
                            SOBRA_C = SOBRA_C%1

    RES_C.append(0)
    RES_C.append(0)

    V100C = int(RES_C[0])
    V50C = int(RES_C[1])
    V20C = int(RES_C[2])
    V10C = int(RES_C[3])
    V5C = int(RES_C[4])
    V2C = int(RES_C[5])

    print("MOEDAS:")
    print("{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01".format   (V1, V50C, V20C, V10C, V5C, V2C))
else:
    print("MOEDAS:")
    print("0 moeda(s) de R$ 1.00")
    print("0 moeda(s) de R$ 0.50")
    print("0 moeda(s) de R$ 0.25")
    print("0 moeda(s) de R$ 0.10")
    print("0 moeda(s) de R$ 0.05")
    print("0 moeda(s) de R$ 0.01")