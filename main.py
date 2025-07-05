from pessoa import Pessoa
from csv_repo import LeitorCSV
from gender_service import Genero
from cep_service import Cep
import json

dados = LeitorCSV().ler_arquivo
servico_genero = Genero()
cep_service = Cep()
pessoas = [Pessoa(dado, gender_service= servico_genero, cep_service = cep_service) for dado in dados]

for pessoa in pessoas:
    pessoa.tratar_nome()
    pessoa.detectar_genero()
    pessoa.detectar_cep()
    pessoa.validar_celular()
    print(pessoa.exibir_info())


pessoas_ordenadas = sorted(pessoas, key=lambda p: p.nomeCompleto.lower())


dados_para_exportar = []
for pessoa in pessoas_ordenadas:
    dados_para_exportar.append({
        "nomeCompleto": pessoa.nomeCompleto,
        "primeiroNome": pessoa.primeiroNome,
        "segundoNome": pessoa.segundoNome,
        "email": pessoa.email,
        "celular": pessoa.celular,
        "cpf": pessoa.cpf,
        "cep": pessoa.cep,
        "interesse": pessoa.interesse,
        "genero": pessoa.genero,
        "bairro": pessoa.bairro,
        "cidade": pessoa.cidade,
        "estado": pessoa.estado,
        "regiao": pessoa.regiao,
        "observacoes": pessoa.observacoes
    })


with open('pessoas_tratadas.json', 'w', encoding='utf-8') as f:
    json.dump(dados_para_exportar, f, ensure_ascii=False, indent=4)

    

    



    


