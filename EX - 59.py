'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1]Somar 
[2]Multiplicação
[3]maior
[4]novos números
[5]Sair do programa

Seu programa deverá realizar a operações soliciada em cada caso.
'''

n1 = int(input('\33[1;32mValor [ 1 ]: \33[m'))
n2 = int(input('\33[1;32mValor [ 2 ]: \33[m'))
soma = 0 
mult = 0
menu = 0
while menu != 5:
    menu = int(input('''\33[1;34m{:=^20}\33[m
[\33[1;33m1\33[m]Soma
[\33[1;33m2\33[m]Multiplicação
[\33[1;33m3\33[m]Maior
[\33[1;33m4\33[m]Novos Números
[\33[1;33m5\33[m]Sair do Programa

OPÇÂO: '''.format(' MENU ')))
    print('\33[1;34m=\33[m'*20)
    if menu == 1:
        soma = n1 + n2 
        print('\33[33mA soma dos valores {} e {} é {}.\33[m'.format(n1 , n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print('A multiplicação entre os valores {} e {} é {}'.format(n1, n2, mult))
    elif menu == 3:
        if n1 == n2: 
            print('Os numeros são iguais !')
        elif n1 > n2 :
            print('Entre {} e {} O valor maior é {}'.format(n1, n2 , n1))
        else:
            print('Entre {} e {} O valor maior é {}'.format(n1 ,  n2 , n2))
    elif menu == 4:
        print('Digite os novos valores!')
        n1 = int(input('Valor [ 1 ]: '))
        n2 = int(input('Valor [ 2 ]: '))