'''
---- DESAFIO 61 ----- 
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma 
PA, mostrando os 10 primeiro termos da progressão usando a estrutura while'''

print('{:=^33}'.format(' Progresão Aritimetrica '))
ter = int(input('Digite o termo: '))
raz = int(input('Digite o razão: '))
dez = ter + (10 - 1 + 1) * raz
print('='*33)
print('(',end='')
while ter != dez :
    print("{}".format(ter), end=',')
    ter += raz
print('...)')
print('='*33)
     
    