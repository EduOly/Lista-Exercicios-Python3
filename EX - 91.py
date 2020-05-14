'''Criei um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionario.No final, coloque esse dicinária em ordem, sabendo que o vencedor tirou o maior número no dado'''
def lin(msg):
    print('\33c')
    print('-'*30)
    print(f'{"|":<}{msg:^28}{"|":>}')
    print('-'*30)

from random import randint
from time import sleep
from operator import itemgetter

org = list()
game = dict()
print('Valores sorteados:')
for c in range(1, 5):
    game[f'Jogador{c}'] = randint(1,6)

for k, v in game.items():
    print(f"   O {k} tirou: {v}")
    sleep(0.90)
org = sorted(game.items(), key=itemgetter(1), reverse=True )
lin('RANKING')
for i, v in enumerate(org):
    print(f'   {i} lugar: {v[0]} com {v[1]}')