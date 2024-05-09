import pandas as pd
import plotly.express as px

tabela = pd.read_csv("JornadaPython\Aula 2 - Python Insights\cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")
tabela = tabela.dropna()

# print(tabela["cancelou"].value_counts(normalize=True))

grafico = px.histogram(tabela, x="duracao_contrato")
grafico.show()