# Análise de Dados - Estudo Complementar

Este repositório contém um conjunto de algoritmos em Python que realizam uma análise de dados em uma tabela de vendas. Essa análise é destinada a fins de estudo e serve como um complemento ao programa anterior, "gera_tabela.py". Os algoritmos utilizam bibliotecas populares, como `pandas`, `matplotlib`, `seaborn`, e `plotly`.

## Conteúdo

1. [Objetivo](#objetivo)
2. [Instruções de Uso](#instruções-de-uso)
3. [Bibliotecas Utilizadas](#bibliotecas-utilizadas)
4. [Algoritmos](#algoritmos)
    - [Importando Bibliotecas](#importando-bibliotecas)
    - [Carregando o DataFrame](#carregando-o-dataframe)
    - [Distribuição de Itens por Loja](#distribuição-de-itens-por-loja)
    - [Proporção de Tamanhos Vendidos](#proporção-de-tamanhos-vendidos)
    - [Estatísticas Descritivas](#estatísticas-descritivas)
    - [Variação do Valor por Loja](#variação-do-valor-por-loja)
    - [Correlação entre Quantidade e Valor](#correlação-entre-quantidade-e-valor)
    - [Distribuição de Tamanhos](#distribuição-de-tamanhos)
    - [Gráfico Interativo com Plotly](#gráfico-interativo-com-plotly)

## Objetivo

O objetivo deste projeto é realizar uma análise exploratória de dados na tabela de roupas gerada anteriormente pelo programa "gera_tabela.py". Essa análise complementar é parte de um estudo mais amplo sobre manipulação e visualização de dados em Python.

## Instruções de Uso

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalar as dependências executando o seguinte comando:
   ```bash
   pip install pandas matplotlib seaborn plotly
   ```
3. Execute o script `analise.py` para realizar a análise de dados.
4. Os gráficos e estatísticas serão exibidos na saída padrão ou salvos em arquivos, conforme especificado no código.

## Bibliotecas Utilizadas

- [pandas](https://pandas.pydata.org/): Manipulação e análise de dados.
- [matplotlib](https://matplotlib.org/): Criação de gráficos estáticos.
- [seaborn](https://seaborn.pydata.org/): Visualizações estatísticas atraentes.
- [plotly](https://plotly.com/): Criação de gráficos interativos.

## Algoritmos

### Importando Bibliotecas
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

### Carregando o DataFrame
```python
df = pd.read_excel('C:\\caminho_do_arquivo\\base.xlsx')
```

### Distribuição de Itens por Loja
```python
plt.figure(figsize=(12, 6))
sns.countplot(x='Loja', hue='Item', data=df)
plt.title('Distribuição de Itens por Loja')
plt.show()
```

### Proporção de Tamanhos Vendidos
```python
tamanho_proporcao = df['Tamanho'].value_counts(normalize=True)
plt.figure(figsize=(8, 8))
plt.pie(tamanho_proporcao, labels=tamanho_proporcao.index, autopct='%1.1f%%', startangle=90)
plt.title('Proporção de Tamanhos Vendidos')
plt.show()
```

### Estatísticas Descritivas
```python
desc_stats = df[['Quantidade', 'Valor']].describe()
print(desc_stats)
```

### Variação do Valor por Loja
```python
plt.figure(figsize=(12, 6))
sns.boxplot(x='Loja', y='Valor', data=df)
plt.title('Variação do Valor por Loja')
plt.show()
```

### Correlação entre Quantidade e Valor
```python
correlation_matrix = df[['Quantidade', 'Valor']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlação entre Quantidade e Valor')
plt.show()
```

### Distribuição de Tamanhos
```python
plt.figure(figsize=(10, 6))
sns.countplot(x='Tamanho', data=df)
plt.title('Distribuição de Tamanhos')
plt.show()
```

### Gráfico Interativo com Plotly
```python
import plotly.express as px

fig = px.scatter(df, x='Quantidade', y='
```

## Autor
[ Lauro Bonometti ]
