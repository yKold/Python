e = input().split()
A = int(e[0])
B = int(e[1])
C = int(e[2])

if A > B and C >= B:
    print(":)")
if A < B and C <= B:
    print(":(")
if A < B and C > B and B-A > C-B:
    print(":(")
if A < B and C > B and B-A <= C-B:
    print(":)")
if A > B and C < B and A-B > B-C: 
    print(":)")
if A > B and C < B and A-B <= B-C: 
    print(":(")
if A == B and C > B:
    print(":)")
if A == B and C <= B:
    print(":(")
