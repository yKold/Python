x = [i for i in range(10)]
for i in range(len(x)):
    y = int(input())
    if y <= 0:
        x[i] = 1
    else:
        x[i] = y
    print(f"X[{i}] = {x[i]}")
