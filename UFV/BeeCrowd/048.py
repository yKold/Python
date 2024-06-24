i = float(input())

if i > 0 and i <= 400:
    reajuste = 15/100
elif i > 400 and i <= 800:
    reajuste = 0.12
elif i > 800 and i <= 1200:
    reajuste = 0.10
elif i > 1200 and i <= 2000:
    reajuste = 0.07
else:
    reajuste = 0.04

novo = reajuste *i

print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %".format(i + novo, novo, reajuste*100))