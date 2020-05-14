#Crie um programa que leia o ano de
#nascimento de sete pesssoas.No final,
#mostre quantas pesoas qinda náo atingiram
#a maioridade e quantos já são maiores
import datetime

maid = 0
menid = 0
atu = datetime.date.today().year

print('{:=^30}'.format(' +18 '))

for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}º pessoas:'))
    id = atu - ano
    if id < 21:
        menid += 1
    elif id >= 21:
        maid += 1
print('='*30)
print(f'''\33[1;31m{menid}\33[m pessoas não atingir a maioridade,
porém \33[1;32m{maid}\33[m pessoas atigirão.''')
print('='*30)
