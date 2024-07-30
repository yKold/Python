x = []
for i in range(10):
    nome = input()
    nota = int(input())
    y = [nome, nota]
    x.append(y)
for j in range(9):
    for i in range(9):
        if x[i+1][1] < x[i][1]:
            a = x[i+1]
            b = x[i]
            x[i+1] = b
            x[i] = a
print(x[0][0], x[9][0])
