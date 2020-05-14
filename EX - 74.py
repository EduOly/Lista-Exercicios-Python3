'''
Crie um programa que vai gerar cinco números
aleatórios e colocar em uma tupla 

Depois disso, mostre a listagem de números
gerados e támbem inque o menor e o maior valor que 
estão na tupla 
'''

from random import randint
tup = ()
for c in range(0, 5):
    print('\33c')
    rand = randint(0, c)
    tup += rand,
print('Os valores soreteados foram:',end='')
for r in tup[0:]:
    print(r, end=' ')
print(f'\nO maior valor sorteado foi {max(tup)}')
print(f'O menor valor sorteado foi {min(tup)}')

