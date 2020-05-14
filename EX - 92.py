'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
icom idade em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
def lin(msg):
    print('\33c')
    print('='*30)
    print(f'{"|":<}{msg:^28}{"|":>}')
    print('='*30)


from datetime import date

lin('FGTS SYS')

pess = dict()
pess['Nome'] = str(input('Nome: '))

ano = int(input('Ano de Nascimento: '))

pess['idade'] = ((date.today().year)-ano)

cart = int(input('Carteira de Trabalho (0 não tem): '))

if cart != 0:
    pess['ctps'] = cart
    pess['contratação'] = int(input('Ano de contração: '))
    pess['salário'] = float(input('Salário: R$'))
    pess['aposentadoria'] = ((35-((date.today().year)-(pess['contratação']))) + pess['idade'])

print('-='*30)

for k, v in pess.items():
    print(f"  --- {k} tem o valor {v}")
print(' ')