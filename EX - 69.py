totm = tot18 = totm20= 0
while True:
    print('-'*30)
    print('{:^30}'.format(' CADRASTRE UMA PESSOA'))
    print('-'*30)
    ida =  int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex =  str(input('Sexo: [M/F]: ')).upper().strip()[0]
        print('-'*30)
        if sex == 'M':
            totm += 1
        if sex == 'F' and ida > 20:
            totm20 += 1
            
        if ida >= 18:
            tot18 += 1
    cond = ' '
    while cond not in 'SN':
        
        cond = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if cond not in'SN':
            print('[ERROR !]')
    if cond == 'N':
            break
print('-'*30)
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totm} homens cadrastrados')
print(f'E temos {totm20} mulheres com mais de 20 anos')