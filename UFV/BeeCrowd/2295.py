e = input().split()
A = float(e[0])
G = float(e[1])
Ra = float(e[2])
Rg = float(e[3])

Ra /= A
Rg /= G

if Ra > Rg:
    print("A")
elif Ra < Rg:
    print("G")
else:
    print("G")