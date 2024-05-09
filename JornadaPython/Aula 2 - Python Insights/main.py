import pandas as pd

tabela = pd.read_csv("JornadaPython\Aula 2 - Python Insights\cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")
tabela = tabela.dropna()
print(tabela.info())