'''
Crie um programa que leia nome, sexo e idade de várias pessoas, quardando os dados de cada pessoas em um dicionário e todos os dicionários em uma lista.No final,mostre:
A)Quantas pessoas foram cadrastradas.
B)A média de idade do grupo.
C)Uma lista com todas as pessoas com idade cima da média.'''
def lin(msg):
    print('\33c')
    print('-'*30)
    print(f'{"|":<}{msg:^28}{"|":>}')
    print('-'*30)

lin('CADRASTRO DE PESSOAS')

pess = dict()
pessoas = list()
sair = ''

while True:
    pess['nome'] = str(input('Nome: '))
    while True:
        pess['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pess['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pess['idade'] = int(input('Idade: '))
    while True:
        sair = str(input('Deseja continuar [S / N]: ')).upper()[0]
        if sair in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
        
    pessoas.append(pess.copy())
    if sair == 'N':
        break
    else:
        print('='*30) 

print('-='*30)
print(f"-- O grupo tem {len(pessoas)} pessoas.")

md = 0
for c in range(0, len(pessoas)):
    md += (pessoas[c]['idade'])
media = md / len(pessoas) 
print(f'-- A Média de idade é {media :.0f} anos.')

mul = list()
for b in range(0, len(pessoas)):
    if pessoas[b]['sexo'] == 'F':
        mul.append(pessoas[b]['nome'])
print(f'-- As mulheres cadastradas foram: ', end='')

for m in mul:
    print(m, end=' ')
print('')
print('-- Lista das pessoas que estã acima da média:')

acmd = list()
for n in range(0, len(pessoas)):
    if pessoas[n]['idade'] >  media:
        acmd.append(pessoas[n])

for c in range(0, len(acmd)):
    print(f"nome = {acmd[c]['nome']}; sexo = {acmd[c]['sexo']} idade = {acmd[c]['idade']}:")
    print(' ')
print('                          <<< ENCERRADO >>>')