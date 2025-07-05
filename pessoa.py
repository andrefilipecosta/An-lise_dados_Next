from gender_service import Genero
from cep_service import Cep
class Pessoa:
    def __init__(self, info:dict, gender_service:Genero, cep_service: Cep):
        self.nomeCompleto = info.get('NomeCompleto','')
        self.email = info.get('Email','')
        self.celular = info.get('Celular','')
        self.cpf = info.get('CPF','')
        self.cep = info.get('CEP','')
        self.interesse = info.get('Interesse','')
        self._primeiroNome = ''
        self.segundoNome = ''
        self._bairro = ''
        self._cidade = ''
        self._estado = ''
        self._regiao = ''
        self._genero = ''
        self.observacoes = []
        self._gender_service = gender_service
        self._cep_service = cep_service 
    
    def tratar_nome(self) -> None:
      
        preposicoes = {'da', 'de', 'do', 'das', 'dos', 'e'}
        palavras = self.nomeCompleto.strip().lower().split()

        nome_formatado = []
        for i, palavra in enumerate(palavras):
            if i == 0:
                nome_formatado.append(palavra.capitalize())
            elif palavra in preposicoes:
                nome_formatado.append(palavra)
            else:
                nome_formatado.append(palavra.capitalize())

        # Atualiza nomeCompleto com espaços e capitalização
        self.nomeCompleto = ' '.join(nome_formatado)

        # Define primeiroNome
        self.primeiroNome = nome_formatado[0]
        
        # Define segundoNome
        if len(nome_formatado) > 1:
            if nome_formatado[1] in preposicoes and len(nome_formatado) > 2:
                self.segundoNome = nome_formatado[1] + ' ' + nome_formatado[2]
            else:
                self.segundoNome = nome_formatado[1]
        else:
            self.segundoNome = ''
    
    @property
    def primeiroNome(self):
        return self._primeiroNome
    
    @primeiroNome.setter
    def primeiroNome(self, valor):
        self._primeiroNome = valor
        
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor
        
    @property
    def bairro(self):
        return self._bairro
    @bairro.setter
    def bairro(self,valor):
        self._bairro = valor
    
    @property
    def cidade(self):
        return self._cidade
    @cidade.setter
    def cidade(self,valor):
        self._cidade = valor
        
    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self,valor):
        self._estado = valor
        
    @property
    def regiao(self):
        return self._regiao
    @regiao.setter
    def regiao(self,valor):
        self._regiao = valor

    def validar_celular(self):
        celular_original = self.celular.strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

        if not celular_original:
            self.observacoes.append('Celular ausente')
            return

        # Remove o "+" caso venha com código internacional
        if celular_original.startswith('+55'):
            celular_original = celular_original[3:]

        # Se tiver menos que 8 ou mais que 11 dígitos, é inválido
        if not celular_original.isdigit() or len(celular_original) < 8 or len(celular_original) > 11:
            self.observacoes.append(f'Celular inválido: {self.celular}')
            return

        ddd = ''
        numero = ''

        if len(celular_original) == 8 or len(celular_original) == 9:
            # Sem DDD → tenta pegar DDD da UF
            ddd_por_estado = {
                'PE': '81', 'SP': '11', 'RJ': '21', 'MG': '31', 'BA': '71',
                'CE': '85', 'DF': '61', 'RS': '51', 'PR': '41', 'SC': '48',
                'GO': '62', 'PA': '91', 'AM': '92', 'ES': '27', 'MA': '98',
                'PB': '83', 'RN': '84', 'AL': '82', 'PI': '86', 'MT': '65',
                'MS': '67', 'RO': '69', 'TO': '63', 'AC': '68', 'AP': '96', 'RR': '95'
            }

            ddd = ddd_por_estado.get(self.estado.upper(), '')
            numero = celular_original
        else:
            ddd = celular_original[:2]
            numero = celular_original[2:]

        # Garante dígito 9 no início se necessário (números móveis têm 9 dígitos)
        if len(numero) == 8:
            numero = '9' + numero

        if len(numero) != 9 or not numero.startswith('9'):
            self.observacoes.append(f'Celular pode estar incompleto: {self.celular}')

        self.celular = f'{ddd} {numero}'
    
    def detectar_genero(self):
        genero = self._gender_service.api_1(self._primeiroNome)
        self.genero = genero
        
    def detectar_cep(self):
        dados = self._cep_service.consulta_cep(self.cep)

        if not dados:
            self.observacoes.append(f'CEP inválido: {self.cep}')
            return

        self.estado = dados.get('estado', '')
        self.cidade = dados.get('cidade', '')
        self.bairro = dados.get('bairro', '')
        self.regiao = dados.get('regiao', '')
        
    
    def exibir_info(self)-> str:
        return f'{self.nomeCompleto} | {self.primeiroNome} | {self.segundoNome} | {self.email}  |{self.celular} | {self.cpf} | {self.cep} | {self.interesse} | GENERO: {self.genero} | Cidade: {self.cidade}'     