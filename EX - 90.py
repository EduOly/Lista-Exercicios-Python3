'''Faça um progrma que leia nome e média de um 
aluno, quardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

print('\33c')

studant = dict()
studant['Name'] = str(input('Nome: '))
studant['Média'] = float(input(f"Média de {studant['Name']}: "))

if studant['Média'] > 5:
    studant['situação'] = 'Aprovado'
else:
    studant['situação'] = 'Reprovado'

for k, v in studant.items():
    print(f"{k} é igual a {v}")

print(' ')

   