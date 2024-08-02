from random import randint
V1 = []
V2 = []
V3 = []
for i in range(150):
    if i <= 74:
        V1.append(randint(0, 100))
    elif i > 74:
        V2.append(randint(0, 100))
for i in range(75):
    V3.append(V1[i] + V2[i])
