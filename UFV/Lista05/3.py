V = []
for i in range(15):
    V.append(int(input()))
M = V.copy()
M.sort()
for i in range(15):
    if V[i] == M[0] or V[i] == M[14]:
        print(i)