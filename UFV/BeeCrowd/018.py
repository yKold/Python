from math import floor
RES = []
SOBRA = 0
VALOR = float(input()) 


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


print("{:.0f}".format(Val))
print("{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(V100, V50, V20, V10, V5, V2, V1))