'''
Melhore o Desafio 61. Peguntando se ele que mostrar mais alguns termos. 
O progrmas encerra quando ele disser que quer mostrar O termos. '''


sn = 0
while sn != 2:
    if sn == 0:
        print('\33[32m{:=^33}\33[m'.format(' PA '))
        ter = int(input('\33[1;33mDigite o Termo: \33[m'))
        raz = int(input('\33[1;33mDigite a Razão: \33[m'))
        dez =  ter + (10 - 1 + 1) * raz 
        print('\33[1;34m=\33[m'*33)
        print('\33[1;32m(', end='')
        while ter != dez:
            print(f'\33[1;32m{ter}\33[m', end=',')
            ter += raz
        print('\33[1;32m...)\33[m')
        print('\33[34m=\33[m'*33) 
    sn = int(input('''\33[1;34m{:=^33}\33[m
    [ \33[1;33m1\33[m ] \33[1;32mNovo PA.\33[m
    [ \33[1;33m2\33[m ] \33[1;31mEXIT.\33[m 
    \33[1;34mOpção: \33[m'''.format(' MENU ')))
    print('\33[1;34m=\33[m'*33)
    if sn == 1 :
        sn = 0        
    elif sn > 2:
        print('\33[1;31m[ERRO] Opção Ivalida!\33[m')


    





    