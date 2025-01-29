from etl import filtrar_produtos_status_entrega, ler_csv, somar_valores_dos_produtos

path_csv = 'vendas.csv'
vendas = ler_csv()
vendas_filtradas = filtrar_produtos_status_entrega(vendas, 'False')
print(somar_valores_dos_produtos(vendas_filtradas))