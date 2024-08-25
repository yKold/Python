from math import sqrt
e = input().split()
L = int(e[0])
A = int(e[1])
P = int(e[2])
R = int(e[3])
D = R*2

H1 = sqrt(L**2 + A**2)
H2 = sqrt(L**2 + P**2)
H3 = sqrt(P**2 + A**2)

if D > L and D > A and D > P and D > H1 and D > H2 and D > H3:
    print("S")
else:
    print("N")