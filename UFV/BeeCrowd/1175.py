x = [0 for i in range(20)]
w = [0 for i in range(20)]
for i in range(20):
    y = int(input())
    x[i] = y
for i in range(20):
    w[19-i] = x[i]
for i in range(20):
    print(f"N[{i}] = {w[i]}")
