print('\33[1;31m[{:=^30}]\33[m'.format(' DESAFIO 50 '))
so = 0
for c in range(0, 6):
    num = int(input('{:^30}'.format(f'Digite o {c}º número: [')))
    if num % 2 == 0:
        so += num
print('-=-'*13)
print('\33[32m{:^20}\33[m'.format(f'Você informou {c}numero e a soma dos pares é  [{so}]'))
print('-=-'*13)