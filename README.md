
# Tutorial: Limpeza, Tratamento e Visualização do Desmatamento na Região Norte do Brasil

## Instalação de Dependências

Certifique-se de ter a biblioteca `basedosdados` instalada. Caso ainda não tenha, utilize o seguinte comando:

```python
!pip install basedosdados
```

## Carregamento dos Dados

```python
import basedosdados as bd

# Carregar os dados diretamente no pandas
df = bd.read_table(dataset_id='br_inpe_prodes',
                  table_id='municipio_bioma',
                  billing_project_id="emissão>")
```

## Limpeza e Tratamento dos Dados

```python
import pandas as pd

# Carregar os dados do arquivo
desmatamento_data = df

# Agrupar os dados por ano
desmatamento_por_ano = desmatamento_data.groupby('ano')['desmatamento_total'].sum()
area_floresta_por_ano = desmatamento_data.groupby('ano')['area_floresta_total'].sum()
```

## Visualização dos Dados

```python
import matplotlib.pyplot as plt

# Criar subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Gráfico para desmatamento total
ax1.plot(desmatamento_por_ano.index, desmatamento_por_ano.values, marker='o', color='red')
ax1.set_title('Evolução do Desmatamento na Região Norte do Brasil (2000-2022)')
ax1.set_ylabel('Área Desmatada (ha)')
ax1.grid(True)

# Gráfico para área de floresta total
ax2.plot(area_floresta_por_ano.index, area_floresta_por_ano.values, marker='s', color='green')
ax2.set_title('Evolução da Área de Floresta na Região Norte do Brasil (2000-2022)')
ax2.set_xlabel('Ano')
ax2.set_ylabel('Área de Floresta (ha)')

# Definir o formato do eixo Y para não usar notação científica
ax2.ticklabel_format(style='plain', axis='y')

ax2.grid(True)

# Ajuste do layout
plt.tight_layout()

# Salvar o gráfico com fundo transparente e em 300 DPI
plt.savefig('desmatamento_floresta_norte_brasil_subplot.png', transparent=True, dpi=300)

# Exibir o gráfico
plt.show()
```

Este tutorial aborda a limpeza, tratamento e visualização do desmatamento na Região Norte do Brasil, utilizando dados do Prodes. Ajuste conforme necessário para seus requisitos específicos.

---

**Nota:** Lembre-se de substituir "emissão>" pelo seu projeto de cobrança no comando `read_table`. Certifique-se de ter as permissões adequadas para acessar os dados.
