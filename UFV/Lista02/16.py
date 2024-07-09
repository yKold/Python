x = int(input())
if x % 3 == 0 and x % 7 == 0:
    print("é divisivel por 3 e 7")
elif x % 3 == 0 and x % 7 != 0:
    print("é divisivel por 3")
else:
    print("é divisivel por 7")