'''
Crie um programa que vai ler vários números e colocar em 
uma lista.
depois disso, mostra:
A)Quantos números foram digitados.
B)A lista de valores, oredenado de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista.
'''
print('\33c')
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja comtinuar? [S / N]: ')).upper()[0]
    if cont in 'N':
        break
print('-='*30)
print(f'Foram digitados {len(lista)} valores. ')
print(f'OS valores decresente e {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'Sim o valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
