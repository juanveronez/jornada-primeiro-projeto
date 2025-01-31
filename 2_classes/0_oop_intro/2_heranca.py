import pandas as pd

class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Método extrair_dados deve ser implementado nas classes filhas.")

    def transformar_dados(self, dados):
        raise NotImplementedError("Método transformar_dados deve ser implementado nas classes filhas.")

    def carregar_dados(self, dados_transformados):
        raise NotImplementedError("Método carregar_dados deve ser implementado nas classes filhas.")

    def executar_etl(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)


class ETLCSV(ETLProcess):
    def __init__(self, fonte_dados, sep=';'):
        if sep != ';':
            print(f"Custom sep: \"{sep}\"")
        
        print('Fonte de dados:', fonte_dados)
        super().__init__(fonte_dados)

    def extrair_dados(self):
        return pd.read_csv(self.fonte_dados)

    def transformar_dados(self, dados):
        # Exemplo simples de transformação: converter todas as letras em maiúsculas
        return dados.map(lambda x: x.upper() if isinstance(x, str) else x)

    def carregar_dados(self, dados_transformados):
        # Aqui você pode implementar a lógica para carregar os dados transformados para onde desejar
        print("Dados transformados:")
        print(dados_transformados)

class ETLExcel(ETLProcess):
    def extrair_dados(self):
        return pd.read_excel(self.fonte_dados)

    def transformar_dados(self, dados):
        # Exemplo simples de transformação: converter todas as letras em maiúsculas
        return dados.map(lambda x: x.lower() if isinstance(x, str) else x)

    def carregar_dados(self, dados_transformados):
        # Aqui você pode implementar a lógica para carregar os dados transformados para onde desejar
        print("Dados transformados:")
        print(dados_transformados)

# Exemplo de uso
if __name__ == "__main__":
    etl_csv = ETLCSV(fonte_dados='exemplo.csv', sep=',')
    etl_csv.executar_etl()