i = input().split()
A = int(i[0])
B = int(i[1])

if A == 0 or B == 0:
    print("Nao sao Multiplos")
else:
    C = A%B
    D = B%A
    if B > A:
        if D == 0:
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")
    if A > B:
        if C == 0:
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")
    if A == B:
        print("Sao Multiplos")
  




