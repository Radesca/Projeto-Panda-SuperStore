# Análise de vendas Superstore com Pandas

Projeto final da disciplina **Python, Ciência de Dados e Pandas** (1º semestre), feito em dupla. É uma análise exploratória do dataset *Sample Superstore*, de vendas de uma varejista.

## O que o script faz

1. Baixa o CSV automaticamente e carrega em um DataFrame.
2. Explora a estrutura dos dados e trata valores faltantes (`Postal Code`).
3. Faz contagens, ordenações e filtros: vendas por categoria, estados com mais pedidos, maiores e menores vendas (`nlargest` e `nsmallest`) e consultas com `query`.
4. Converte datas e extrai ano e mês, para totalizar as vendas por período.
5. Calcula análises numéricas sobre a série mensal de vendas.
6. Monta uma tabela cruzada (`crosstab`) de **região × categoria**.
7. Gera gráficos com seaborn e matplotlib:
   - total de vendas por categoria;
   - total de vendas por região;
   - evolução das vendas mês a mês.

## Como rodar

Requer Python 3.9 ou superior.

```bash
pip install pandas matplotlib seaborn
python Projeto_Pandas_Superstore.py
```

O script baixa `superstore.csv` na pasta atual e salva uma cópia em `superstore_copia.csv`. Também funciona em Jupyter ou Google Colab.

## Tecnologias

Python, pandas, matplotlib e seaborn.
