x = int(input())
y = []
w = 0
y.append(1)
for i in range(x):  
    y.append(w)
    w += y[i]
y.remove(y[0])
res = " ".join(map(str, y))
print(res)