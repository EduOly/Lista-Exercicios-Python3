print('\33[1;32m{:=^35}\33[m'.format(' PA '))
#Entrada
ter = int(input('Digite o termo: '))
ras = int(input('Razão: '))
dez = ter + (10 - 1) * ras
#condição
print('='*35)
print('(',end='')
for c in range(ter, dez + ras, ras):#Está multiplicado a razão pra da um PA de 10 primeiros
    print(f"{c}", end=', ')#Saida
print(')',end='')

#-----DESAFIO 51------
#Desenvolva um programa que leia o primeiro
#termo e a razão de uma PA. No final, mostre
#as 10 primeiros termos.