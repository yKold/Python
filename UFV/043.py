i = input().split()
A = float(i[0])
B = float(i[1])
C = float(i[2])

if A+B>C and A+C>B and B+C>A:
    perimetro = A+B+C
    print(f"Perimetro = {perimetro}")
else:
    area = (A+B)*C /2
    print(f"Area = {area}")