mes = int(input())
valor_trimestre = 3
trimestre = 1
for index in range(mes):
    if index+1 <= valor_trimestre :
        if mes == index+1:
            print(f"O mês {index+1} está no {trimestre} trimestre")
    else:
        valor_trimestre += 3
        trimestre += 1
        if mes == index+1:
            print(f"O mês {index+1} está no {trimestre} trimestre" )

