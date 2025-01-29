import csv

caminho_arquivo: str = 'exemplo.csv'

dados: list = []

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
  dictReader = csv.DictReader(arquivo)

  for linha in dictReader:
    dados.append(linha)

print(dados)