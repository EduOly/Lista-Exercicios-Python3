'''
Crie um progrma onde o usário possa
digitar vários valores numéricos e cadrastre-os em
uma lista.Caso o número já axista lá dentro, ele
não será adicionado.No final, serão exibidos todos 
os valores únicos digitados, em ordem crescente.
'''
print('\33c')
print('\33[1;34m-\33[1;33m'*40)
print(f'\33[1;32m{":":<0}\33[m\33[1;32m{"CADRASTRO NUMÈRICOS":^38}\33[m\33[1;32m{":":>0}\33[m')
print('\33[1;34m-\33[m'*40)
valor = []
while True:
    n = int(input('Digite O valor: '))
    if n not in valor:
        valor.append(n)
    else:
        print('Valor duplicado! não adicionado...')
    r = str(input('Deseja continuar?: [S / N] ')).upper()[0]
    if r in 'N':
        break
print('-'*40)
print(f'O banco de dados dos valores forão: ')
print('-'*40)
print(f'{sorted(valor)}')