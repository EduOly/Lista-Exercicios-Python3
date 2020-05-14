from time import sleep
from random import randint
#Entrada de dados
num = int(input('''\33[34m{:=^20}
{:-^20}
{:-^20}
{:-^20}
{}\33[m'''.format(' MENU ', '[0] PEDRA ', '[1] PAPEL', '[2]TESOURA', 'Qual é a sua Jogador: ')))
print('JÓ')
sleep(1)
print('KEM')
sleep(1)
print('PÒ!!!')
#Variaveis
pc = randint(0, 2)
lista = ['Pedra', 'Papel', 'Tesoura']
print('-=-'*15)
print(f'Você escolheu \33[32m{lista[num]}\33[m e computador  \33[31m{lista[pc]}\33[m')
print('-=-'*15)
if pc == 0:
    if num == 0:
        print('EMPATE')
    elif num == 1 :
        print('Você ganhou!')
    elif num == 2 :
        print('Computador ganhou!')
elif pc == 1:
    if num == 1:
        print('EMPATE')
    elif num == 0:
        print('Computador ganho!')
    elif num == 2:
        print('Você ganhou!')
elif pc == 2:
    if num == 2:
        print('EMPATE')
    elif num == 0:
        print('Eu ganhou!')
    elif num == 1:
        print('Computador ganhau!')
    else:
        print('Opção invalida!!')