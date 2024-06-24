N = int(input())

if not N<=10000 and not N>=1:
    N = int(input())

Res = []

for i in range(0, 10001):
    if i%N == 2:
        Res.append(i)
        
for i in range(len(Res)):
    print(Res[i])