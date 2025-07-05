import requests
from typing import Dict

class Cep:

    def __init__(self):
        self.apiUrl = 'https://viacep.com.br/ws'

    def consulta_cep(self, cep: str) -> Dict[str, str]:
        
        cep = cep.strip().replace('-', '').replace(' ', '')

        
        if len(cep) != 8 or not cep.isdigit():
            return {}

        url = f'{self.apiUrl}/{cep}/json/'

        try:
            resposta_api = requests.get(url)
            resposta_api.raise_for_status()
            dados = resposta_api.json()

            
            if 'erro' in dados:
                return {}

            
            return {
                "estado": dados.get("uf", ''),
                "cidade": dados.get("localidade", ''),
                "bairro": dados.get("bairro", ''),
                "regiao": '' 
            }

        except requests.RequestException as e:
            print(f"Erro ao consultar o CEP: {e}")
            return {}