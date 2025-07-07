import pandas as pd

# 🧾 Carrega os dados
df = pd.read_json('pessoas_tratadas.json', encoding='utf-8')

print('\n--- 📊 DISTRIBUIÇÃO DE GÊNERO ---')
genero_dist = df['genero'].value_counts(normalize=True).mul(100).round(2)
print(genero_dist.to_string())

print('\n--- 🗺️ DISTRIBUIÇÃO POR REGIÃO ---')
regiao_dist = df['regiao'].replace('', 'Não informado').value_counts(normalize=True).mul(100).round(2)
print(regiao_dist.to_string())

print('\n--- 🚦 QUALIDADE DOS DADOS ---')

# ➤ CPFs inválidos: menos de 11 dígitos
df['cpf_limpo'] = df['cpf'].str.replace(r'\D', '', regex=True)
cpfs_invalidos = df[df['cpf_limpo'].str.len() != 11]
print(f'CPFs inválidos: {len(cpfs_invalidos)}')

# ➤ Telefones ausentes ou incompletos
df['celular_limpo'] = df['celular'].str.replace(r'\D', '', regex=True)
sem_celular = df[df['celular_limpo'].str.len() < 10]
print(f'Telefones ausentes ou incompletos: {len(sem_celular)}')

# ➤ CEPs inválidos detectados via observações
com_erro_cep = df[df['observacoes'].apply(lambda obs: any('CEP inválido' in o for o in obs))]
print(f'CEPs inválidos: {len(com_erro_cep)}')

import pandas as pd

df = pd.read_json('pessoas_tratadas.json', encoding='utf-8')

# ⚖️ Agrupa por gênero → conta interesses → normaliza → pega top 5
preferencias_top5 = (
    df.groupby('genero')['interesse']
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
    .groupby(level=0, group_keys=False)
    .nlargest(5)
)

#  Exibe resultado
print('\n--- 🎯 TOP 5 ÁREAS DE INTERESSE POR GÊNERO ---\n')
for genero in preferencias_top5.index.levels[0]:
    print(f'> {genero}\n')
    filtro = preferencias_top5[genero]
    print(filtro.to_string())
    print('\n' + '-' * 40 + '\n')