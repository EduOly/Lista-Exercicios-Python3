'''Faça um programa que ajude um jogandor
da MEGA SENA  a criar palpites.O programa
vai pergunte quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60 para cada
jogo, cadrastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

lista = list()
const = 0
game = []
print('\33c')
print('\33[1;32m-'*40)
print(f"{'|':<0}\33[1;33m{'MEGA SENA':^38}\33[m\33[1;32m{'|':>1}")
print(f'-'*40)
print('\33[m '*10)

jogos = int(input('Quantos jogos quer que eu sorteie?: '))

cont = 0
for c in range(0, jogos):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1 
        if cont >= 6:
            break
    game.append(lista[:])
    lista.clear()
    cont = 0

print('-'*37)
print(f"{'|':<10}{'SORTEANDO':^2}{jogos:^3}{'JOGOS':^2}{'|':>10}")
print('-'*37)
print(' '*10)

for e in range(0, jogos):
    print(f'Jogo {e+1}: {sorted(game[e])}')
    sleep(0.7)
print('-'*37)
print(' '*10)