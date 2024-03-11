import random

a = []

while len(a) < 6:
    k = random.randint(1, 60)
    if k not in a:
        a.append(k)

for i in range(len(a)):
    print("No número {}, o valor é: {}".format(i+1, a[i]))
