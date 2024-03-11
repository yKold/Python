pessoas = list()
pessoa = {
    "nome": "Gabriel",
    "sexo": "M",
    "idade": 17
}
print("------------------------------------")
print(pessoa.keys())
print("------------------------------------")
print(pessoa.values())
print("------------------------------------")
print(pessoa.items())
print("------------------------------------")
pessoas.append(pessoa.copy())
print(pessoas)