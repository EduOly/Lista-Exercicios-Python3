'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocálos dentro da lista e segunda função vai mostra a soma entre todos os valores PARES sorteados pela função anterior'''

print('\33c')
from time import sleep
from random import randint

def sorteio(num):
    for c in range(0, 5):
        num.append(randint(0, 6))
    print(f"Sorteamos 5 valores da lista: ",end='')
    for g in num:
        print(g, end=' ', flush=True)
        sleep(0.4)
    print('PRONTO!')

def soma_PAR(som):
    soma = 0
    for j in som:
        if j % 2 == 0:
            soma += j
    print(f"Somando os valores pares de {som}, temos {soma}.")
    print('-='*30)
    

    
numeros = list() 

sorteio(numeros)
soma_PAR(numeros)
