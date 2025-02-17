import pandas as pd

planilha1 = pd.read_excel(r'C:\Users\galat\Downloads\planilhas\produto1.xlsx')
planilha2 = pd.read_excel(r'C:\Users\galat\Downloads\planilhas\produto2.xls')

coluna_descricao = 'Descrição'
coluna_valor = 'Valor'

for index, row in planilha1.iterrows():
    descricao_valor = row[coluna_descricao]
    valor = row[coluna_valor]

    if descricao_valor in planilha2[coluna_descricao].values:
        planilha2.loc[planilha2[coluna_descricao] == descricao_valor, coluna_valor] = valor

caminho_saida = r'C:\Users\galat\Downloads\planilhas\planilha2_atualizada.xlsx'
planilha2.to_excel(caminho_saida, index=False)

print("Planilha 2 atualizada com sucesso!")