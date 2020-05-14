from math import sqrt
print('\33[1;31m-=-\33[m'*10)
print('{:=^40}'.format(' \33[1;32mMUt \33[m'))
print('\33[1;31m-=-\33[m'*10)
num = int(input('Informe um número: '))
r = sqrt(num)
print('O dobro de \33[1;32m{}\33[m é \33[1;32m{}\33[m, \no triplo '
      'é \33[1;32m{}\33[m e a raiz é \33[1;32m{:.0F}\33[m .'.format(num, num*2, num*3 , r))
print('\33[1;31m-=-\33[m'*10)