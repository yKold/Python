Salary = float(input())
Resto = 1
Taxa = 0

if Salary > 0 and Salary <= 2000:
    Taxa = "Isento"
    print(Taxa)
elif Salary > 2000 and Salary <= 3000:
    Salary -= 2000
    Taxa = 0.08
    Salary *= Taxa
    print("R$ {:.2f}".format(Salary))
elif Salary > 3000 and Salary <= 4500:
    Salary -= 3000
    Taxa = 0.18
    Salary *= Taxa
    Salary += 1000*0.08
    print("R$ {:.2f}".format(Salary))
else:
    Salary -= 4500
    Taxa = 0.28
    Salary *= Taxa
    Salary += 1500 * 0.18
    Salary += 1000 * 0.08
    print("R$ {:.2f}".format(Salary))