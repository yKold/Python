i = input().split()
A = int(i[0])
B = int(i[1])

Dia = 24

if A == B:
    print("O JOGO DUROU 24 HORA(S)")

if A>B:
    Dia -= A
    Dia += B
    print(f"O JOGO DUROU {Dia} HORA(S)")
if B>A:
    B -= A
    print(f"O JOGO DUROU {B} HORA(S)")

