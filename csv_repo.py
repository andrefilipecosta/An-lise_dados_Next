import csv

class LeitorCSV:
    """
    classe com o caminho do arquivo csv como uma constante,
    que retorna uma lista de dicionarios com as informações brutas do arquivo csv
    """
    CAMINHO_PADRAO = r'C:\temp\python\projetos\analise_dados\src\data\lista_clientes.csv'

  
    def __init__(self):
        self.caminho = self.CAMINHO_PADRAO
        self.ler_arquivo = self.ler_arquivo()
      
        

    def ler_arquivo(self):

        """
        Lê o arquivo CSV e cria um dicionario com os dados do arquivo .

        Trata erro como arquivo não encontrado.
        """
        caminho = self.CAMINHO_PADRAO
        try:
            with open(caminho, newline='', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)
                lista =[]
                for linha in leitor:
                    lista.append(linha)       
           
            return lista        
        except FileNotFoundError:
            print(f'Arquivo não encontrado: {caminho}')
            return []
        

# Exemplo de uso:


"""if __name__ == '__main__':
    
    dados = LeitorCSV()
    
    for dado in dados.dados:
        print(dado)
"""        
    