x = [i for i in range(10)]
y = int(input())
for i in range(len(x)):
    x[i] = y
    y *= 2
    print(f"N[{i}] = {x[i]}")