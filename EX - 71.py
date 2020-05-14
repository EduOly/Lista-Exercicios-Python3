print('-'*40)
print('{:^40}'.format(' BANCO INTER '))
print('-'*40)
valor = int(input('Informe o valor: R$ '))
totced = 0
ced = 50
while True: 
    if valor >= ced:
        valor -= ced 
        totced += 1
    else: 
        if totced > 0:
            print(f'Seram {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break
print('-'*40)
print('Volte sempre!, tenha um exelente Dia !')