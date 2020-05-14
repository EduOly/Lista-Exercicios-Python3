'''
Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: incio, fim e passo e realize a 
contagem.
Seu programa tem que realizar três contagens através da função 
criada:
A)De 1 até 10, de 1 em 1
B)De 10 até 0, de 2 em 2
C)Uma contagem pesonalizada. '''

print('\33c')
from time import sleep

def contador(i, f, p):
    print('~'*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    for c in range(i, f, p):
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)
    print('FIN!')
    
#programa princinpal

contador(1, 10 , 1)
contador(10, 0, -2)

print('-='*20)
inicio =int(input('Digite o valor inicial: '))
fim =  int(input('Digite o valor final: '))
passos = int(input('Digite os passos: '))
print('-='*20)

contador(inicio, fim, passos)
print( )