import csv

def ler_csv(caminho_csv) -> list[dict]:
  """
  Função que lê um arquivo CSV e retorna uma lista de dicionários.
  """

  data = []
  with open(caminho_csv, 'r', encoding='utf-8') as file:
    for row in csv.DictReader(file):
      data.append(row)
  
  return data
  
def filtrar_produtos_status_entrega(
  lista_vendas: list[dict],
  status_entrega: str = 'True'
) -> list[dict]:
  """
  Filtra os produtos pelo status da entrega
  """
  return [
    item for item in lista_vendas
    if item.get('Entregue') == status_entrega
  ]


def somar_valores_dos_produtos(lista_vendas: list[dict]) -> int:
  """
  Soma os valores dos produtos
  """
  total = 0
  for item in lista_vendas:
    total += int(item.get('Venda'))
  
  return total
