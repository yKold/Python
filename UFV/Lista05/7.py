V = [i for i in range(50)]
for i in range(25):
    x = V[i]
    y = V[49-i]
    V[i] = y
    V[49-i] = x
print(V)