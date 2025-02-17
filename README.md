# Atualização de Planilha de Produtos

Este script Python foi desenvolvido para facilitar a atualização de uma planilha de produtos (`produto2.xls`) com base nos dados de outra planilha (`produto1.xlsx`). O script compara as descrições dos produtos nas duas planilhas e, quando encontra uma correspondência, atualiza o valor do produto na segunda planilha com o valor da primeira.

## Requisitos
Para utilizar este script, é necessário ter instalado:
- Python 3.x
- Pandas: Biblioteca para manipulação de dados.
- Openpyxl: Biblioteca para leitura e escrita de arquivos Excel.

## Instalação das Dependências
Antes de executar o script, instale as bibliotecas necessárias utilizando o seguinte comando:

```bash
pip install pandas openpyxl
```

## Como Usar
### 1. Preparando as Planilhas:
- Certifique-se de que as planilhas `produto1.xlsx` e `produto2.xls` estão localizadas no diretório especificado no código (`C:\Users\galat\Downloads\planilhas\`).
- Ambas as planilhas devem conter as colunas `Descrição` e `Valor` para que a atualização ocorra corretamente.

### 2. Executando o Script:
O script irá:
1. Ler as duas planilhas.
2. Comparar as descrições dos produtos.
3. Atualizar os valores na `produto2.xls` com base nos valores da `produto1.xlsx`.
4. Salvar a `produto2.xls` atualizada como `planilha2_atualizada.xlsx` no mesmo diretório.

### 3. Verificando a Saída:
Após a execução, o script gerará um novo arquivo `planilha2_atualizada.xlsx` com os valores atualizados. Além disso, imprimirá uma mensagem no console informando que a atualização foi concluída com sucesso.

## Estrutura do Código
### 1. Leitura das Planilhas:
```python
import pandas as pd

planilha1 = pd.read_excel(r'C:\Users\galat\Downloads\planilhas\produto1.xlsx')
planilha2 = pd.read_excel(r'C:\Users\galat\Downloads\planilhas\produto2.xls')
```

### 2. Iteração e Atualização:
```python
for index, row in planilha1.iterrows():
    descricao_valor = row['Descrição']
    valor = row['Valor']

    if descricao_valor in planilha2['Descrição'].values:
        planilha2.loc[planilha2['Descrição'] == descricao_valor, 'Valor'] = valor
```

### 3. Salvamento da Planilha Atualizada:
```python
caminho_saida = r'C:\Users\galat\Downloads\planilhas\planilha2_atualizada.xlsx'
planilha2.to_excel(caminho_saida, index=False)
```

### 4. Mensagem de Conclusão:
```python
print("A planilha foi atualizada com sucesso e salva como 'planilha2_atualizada.xlsx'!")
```

## Observações
- Certifique-se de que os caminhos dos arquivos estão corretos e que você possui permissão para leitura e escrita nos arquivos.
- O script **não modifica** a `planilha1.xlsx`, apenas a `planilha2.xls`, que será salva como um novo arquivo.

## Contribuições
Contribuições são bem-vindas! Caso tenha sugestões ou melhorias, abra uma issue ou envie um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

