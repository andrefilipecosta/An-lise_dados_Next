import requests


class Genero:
    
    def __init__(self):
        self.api_url = 'https://api.genderize.io'
 
        
    def api_1(self, primeiroNome):
        
        nome = primeiroNome 
        url = f'https://api.genderize.io?name={nome}'
        resposta_api = requests.get(url).json()
        genero = resposta_api['gender']
        
        if genero == 'male':
            genero = 'Masculino'
            return genero
        elif genero == 'female':
            genero = 'Feminino'
            return genero
        
        
            
            
        
        
        
        
        