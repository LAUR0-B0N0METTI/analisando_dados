# Importando bibliotécas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar o DataFrame do arquivo Excel
df = pd.read_excel('C:\\caminho_do_arquivo\\tabela_roupas.xlsx')


# Visualizar a quantidade de cada tipo de item em cada loja
plt.figure(figsize=(12, 6))
sns.countplot(x='Loja', hue='Item', data=df)
plt.title('Distribuição de Itens por Loja')
plt.show()


# Calcular a proporção de cada tamanho vendido
tamanho_proporcao = df['Tamanho'].value_counts(normalize=True)


# Visualizar a proporção de tamanhos em um gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(tamanho_proporcao, labels=tamanho_proporcao.index, autopct='%1.1f%%', startangle=90)
plt.title('Proporção de Tamanhos Vendidos')
plt.show()


# Calcular médias, medianas, desvio padrão, etc.
desc_stats = df[['Quantidade', 'Valor']].describe()


# Imprimir as estatísticas descritivas
print(desc_stats)


# Visualizar a variação de preços entre as lojas
plt.figure(figsize=(12, 6))
sns.boxplot(x='Loja', y='Valor', data=df)
plt.title('Variação do Valor por Loja')
plt.show()


# Calcular a matriz de correlação
correlation_matrix = df[['Quantidade', 'Valor']].corr()


# Visualizar a matriz de correlação em um heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlação entre Quantidade e Valor')
plt.show()


# Visualizar a distribuição dos valores da coluna [Tamanho]
plt.figure(figsize=(10, 6))
sns.countplot(x='Tamanho', data=df)
plt.title('Distribuição de Tamanhos')
plt.show()


# Importando bibliotéca "Plotly"
import plotly.express as px


# Criar um gráfico interativo com Plotly
fig = px.scatter(df, x='Quantidade', y='Valor', color='Loja', size='Quantidade', hover_data=['Item'])


# Exibir o dashboard interativo
fig.show()
