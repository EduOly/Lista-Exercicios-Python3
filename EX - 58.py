'''
Melhore o desafio 28 onde o computador vai 
"pensar" em um número entre 0 e 10. Só que agora o jogador 
vai tentar adivinhar até acerta, mostrando no final quantos 
palpites foram necessários para vencer.
'''
from random import randint
computador  = randint(0, 10)
print('Sou seu Computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que voçê consegue adivinhar qual foi? ')
acertou = False
pal = 0
while  not acertou:
    jogador = int(input('Qual é seu palpite?: ' ))
    pal += 1 
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAis...')
        elif  jogador > computador:
            print('Menos...')
print('Acertou com {} palpites'.format(pal))
