from math import trunc
print('{:=^30}'.format(' TRUNC '))
num  = float(input('Informe um número real: '))
nu = trunc(num)
print('O valor de {} ficará assim :{}'.format(num, nu))
print('='*30)