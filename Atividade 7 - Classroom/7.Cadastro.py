pessoas = []
total_cadastradas = 0
soma_idades = 0
mulheres_cadastradas = []
idades_acima_da_media = []

while True:
    usuario = {}
    usuario['nome'] = input('Digite o nome do usuário (ou "sair" para encerrar o sistema): ').strip()
    if usuario['nome'].lower() == 'sair':
        break

    usuario['sexo'] = input('Digite o sexo da pessoa (M/F): ').strip().upper()
    usuario['idade'] = int(input('Digite a idade da pessoa: '))
    pessoas.append(usuario)
    total_cadastradas += 1
    soma_idades += usuario['idade']
    
    if usuario['sexo'] == 'F':
        mulheres_cadastradas.append(usuario['nome'])
    
media_idade = soma_idades / total_cadastradas
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        idades_acima_da_media.append(pessoa['nome'])

print(f'\nForam cadastradas {total_cadastradas} pessoas.')
print(f'A média de idade é {media_idade:.2f} anos.')
print(f'Mulheres cadastradas: {", ".join(mulheres_cadastradas)}')
print(f'Pessoas com idade acima da média: {", ".join(idades_acima_da_media)}')
