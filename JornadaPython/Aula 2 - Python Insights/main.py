import pandas as pd
import plotly.express as px

tabela = pd.read_csv("JornadaPython\Aula 2 - Python Insights\cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")
tabela = tabela.dropna()

# print(tabela["cancelou"].value_counts(normalize=True))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()