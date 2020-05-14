'''Faça um progrma que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analizar todos os valores e dizer qual
deles é o maior'''

print('\33c')

from time import sleep

def maior(*num):
    print('-='*30)
    print('Analizado os valores passados...')
    sleep(1)
    for c in num:
       print(c, end=' ', flush=True)
       sleep(0.5)
    print(f'Foram informado {len(num)} valores ao todo.')
    sleep(1)
    print(f"O maior valor informado foi {max(num)}.")
 
#Progrma principal

maior(2,9,4,5,7,1)
maior(4,7,0,7)
maior(1,2)
maior(6)
maior(0)
print( )