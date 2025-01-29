produtos: list[dict[str]] = []

produto_1: dict[str] = {
  "nome": "Sapato",
  "quantidade": 4,
  "preco": 10.32,
  "disponivel": True
}

produto_2: dict[str] = {
  "nome": "Computador",
  "quantidade": 2,
  "preco": 1359.99,
  "disponivel": False
}

produtos.append(produto_1)
produtos.append(produto_2)

for produto in produtos:
  info = produto.items()
  print(info)