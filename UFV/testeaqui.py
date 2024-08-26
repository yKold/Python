qtd = 0
V = []
for i in range(25):
    V.append(int(input()))
guarda = []
for i in range(25):
    for j in range(25):
        if i!=j and V[i] == V[j] and V[i] !=0:
            guarda.append(V[i])
for i in range(len(V)):
    for j in range(len(V)):
        if i!=j and V[i] == V[j]:
            qtd +=1
    print(i, qtd)
    qtd=0