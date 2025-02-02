import pandas as pd

def carregar_csv_e_filtrar(arquivo_csv, estado):
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv(arquivo_csv)
    
    # Verificar e remover células vazias
    df = df.dropna()
    
    # Filtrar as linhas pela coluna estado
    df_filtrado = df[df['estado'] == estado]
    
    return df_filtrado

if __name__ == '__main__':
    df_filtrado = carregar_csv_e_filtrar(arquivo_csv='./exemplo.csv', estado='SP')
    print(df_filtrado)