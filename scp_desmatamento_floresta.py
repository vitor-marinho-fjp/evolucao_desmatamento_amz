# Script para Limpeza, Tratamento e Visualização do Desmatamento na Região Norte do Brasil

# Instalação de Dependências
pip install basedosdados

# Carregamento dos Dados
import basedosdados as bd

df = bd.read_table(dataset_id='br_inpe_prodes',
                  table_id='municipio_bioma',
                  billing_project_id="emissão>")

# Limpeza e Tratamento dos Dados
import pandas as pd

desmatamento_data = df
desmatamento_por_ano = desmatamento_data.groupby('ano')['desmatamento_total'].sum()
area_floresta_por_ano = desmatamento_data.groupby('ano')['area_floresta_total'].sum()

# Visualização dos Dados
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(desmatamento_por_ano.index, desmatamento_por_ano.values, marker='o', color='red')
ax1.set_title('Evolução do Desmatamento na Região Norte do Brasil (2000-2022)')
ax1.set_ylabel('Área Desmatada (ha)')
ax1.grid(True)

ax2.plot(area_floresta_por_ano.index, area_floresta_por_ano.values, marker='s', color='green')
ax2.set_title('Evolução da Área de Floresta na Região Norte do Brasil (2000-2022)')
ax2.set_xlabel('Ano')
ax2.set_ylabel('Área de Floresta (ha)')

ax2.ticklabel_format(style='plain', axis='y')

ax2.grid(True)

plt.tight_layout()

plt.savefig('desmatamento_vs_floresta.png', transparent=True, dpi=300)

plt.show()
