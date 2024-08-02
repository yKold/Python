from random import randint
V = []
for i in range(100): 
    R = randint(0, 10)
    V.append(R)
N = int(input())
for i in V:
    if i == N:
        print("existe")