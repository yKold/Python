n = int(input())
for i in range(n):
    x = input().split()
    x1 = list(x[0])
    x2 = list(x[1])
    while len(x1) > len(x2):
        x2.append("0")
    while len(x2) > len(x1):
        x1.append("0")
    res = []
    for i in range(len(x1)):
        res.append(x1[i])
        res.append(x2[i])
    resF = "".join(res)
    fim = resF.replace("0", "")
    print(fim)