# =============================================================================
# Projeto Final - Disciplina "Python, Ciência de Dados e Pandas" - 1º Semestre
# Natan de Paulo Gonçalves Torres  | RA: 2511551211
# Henrique dos Santos Radesca       | RA: 2511550794
# =============================================================================

# ── Instalação das dependências (rodar apenas se necessário) ──────────────────
# !pip install pandas matplotlib seaborn

import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# CONFIGURAÇÕES DE EXIBIÇÃO
# =============================================================================

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print("Pandas versão:", pd.__version__)

# =============================================================================
# DOWNLOAD E LEITURA DO DATASET
# =============================================================================

# Download automático do arquivo CSV (Sample Superstore)
url_csv = (
    'https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis'
    '/main/Sample%20-%20Superstore.csv'
)
urllib.request.urlretrieve(url_csv, 'superstore.csv')

# Lê o CSV e cria o DataFrame
df = pd.read_csv('superstore.csv', sep=',', encoding='iso-8859-1')

# Exporta uma cópia do dataset original
df.to_csv('superstore_copia.csv', index=False)

# =============================================================================
# EXPLORAÇÃO INICIAL
# =============================================================================

print("\n── Shape ──")
print('Quantidade de Linhas e Colunas:', df.shape)
print(df.shape[0], 'linhas')
print(df.shape[1], 'colunas')

print("\n── Colunas ──")
print(df.columns)

print("\n── Info ──")
df.info()

print("\n── Valores nulos por coluna ──")
print(df.isna().sum())

print("\n── Tipos de dados ──")
print(df.dtypes)

# =============================================================================
# TRATAMENTO DE DADOS FALTANTES
# =============================================================================

# Preenche valores nulos da coluna Postal Code com 0 (boa prática)
df['Postal Code'] = df['Postal Code'].fillna(0)

# =============================================================================
# ANÁLISE EXPLORATÓRIA: CONTAGENS, ORDENAÇÕES E FILTROS
# =============================================================================

print("\n── Quantidade de vendas por categoria ──")
print(df['Category'].value_counts())

print("\n── Estados com maior número de pedidos ──")
print(df['State'].value_counts())

print("\n── Top 10 maiores vendas ──")
print(df.sort_values(by='Sales', ascending=False).head(10))

print("\n── nlargest: Top 10 maiores vendas ──")
print(df.nlargest(10, 'Sales'))

print("\n── nsmallest: 10 menores vendas ──")
print(df.nsmallest(10, 'Sales'))

print("\n── Query: somente categoria Technology ──")
print(df.query("Category == 'Technology'"))

print("\n── Query: vendas acima de $1.000 ──")
print(df.query("Sales > 1000"))

# =============================================================================
# CONVERSÃO DE DATAS E EXTRAÇÃO DE ANO / MÊS
# =============================================================================

# Converte Order Date e Ship Date para datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

# Extrai Ano e Mês
df['Ano'] = df['Order Date'].dt.year
df['Mes'] = df['Order Date'].dt.month

print("\n── Amostra: Order Date, Ano, Mês ──")
print(df[['Order Date', 'Ano', 'Mes']].head())

print("\n── Quantidade de pedidos por ano ──")
print(df['Ano'].value_counts())

print("\n── Soma de vendas por ano ──")
vendas_ano = df.groupby('Ano')['Sales'].sum()
print(vendas_ano)

# Cria coluna Ano-Mês
df['AnoMes'] = df['Order Date'].dt.to_period('M')

print("\n── Amostra: Order Date, AnoMes ──")
print(df[['Order Date', 'AnoMes']].head())

# =============================================================================
# ANÁLISES NUMÉRICAS SOBRE A SÉRIE MENSAL DE VENDAS
# =============================================================================

vendas_mes = df.groupby('AnoMes')['Sales'].sum()

print("\n── Vendas por mês ──")
print(vendas_mes)

print("\n── diff(): variação absoluta mês a mês ──")
print(vendas_mes.diff())

print("\n── pct_change(): variação percentual mês a mês ──")
print(vendas_mes.pct_change())

print("\n── cumsum(): acumulado de vendas ──")
print(vendas_mes.cumsum())

print("\n── rolling(3).mean(): média móvel de 3 meses ──")
print(vendas_mes.rolling(3).mean())

print("\n── rolling(3).sum(): soma móvel de 3 meses ──")
print(vendas_mes.rolling(3).sum())

# =============================================================================
# TABELA CRUZADA (CROSSTAB) — REGIÃO × CATEGORIA
# =============================================================================

print("\n── Crosstab: Região × Categoria ──")
print(pd.crosstab(df['Region'], df['Category']))

print("\n── Crosstab transposta ──")
print(pd.crosstab(df['Region'], df['Category']).transpose())

print("\n── Crosstab empilhada (stack) ──")
print(pd.crosstab(df['Region'], df['Category']).stack())

# =============================================================================
# VISUALIZAÇÕES GRÁFICAS
# =============================================================================

sns.set_style('whitegrid')

# Gráfico 1 — Total de vendas por categoria
vendas_categoria = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=vendas_categoria.index, y=vendas_categoria.values)
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Total de Vendas (Sales)')
plt.tight_layout()
plt.show()

# Gráfico 2 — Total de vendas por região
vendas_regiao = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=vendas_regiao.index, y=vendas_regiao.values)
plt.title('Total de Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Total de Vendas (Sales)')
plt.tight_layout()
plt.show()

# Gráfico 3 — Evolução das vendas mês a mês
plt.figure(figsize=(12, 5))
vendas_mes.plot(kind='line', marker='o')
plt.title('Evolução das Vendas por Mês (Ano-Mês)')
plt.xlabel('Ano-Mês')
plt.ylabel('Total de Vendas (Sales)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
