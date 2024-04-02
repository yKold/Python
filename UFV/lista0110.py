from math import log
r = int(input("r: "))
an = int(input("an: "))
a1 = int(input("a1: "))
n = (log(an) - log(a1))/ log(r) + 1
print(n)