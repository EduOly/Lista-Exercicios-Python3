
print('{:=^30}'.format(' \33[32mColégio Salvador\33[m '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

md = (n1+n2)/2
print('-=-'*7)
if md < 5.0:
    print('\33[1;31m[{:^20}]\33[m'.format(' Reprovado '))
elif md >= 5.0 and md <= 6.9:
    print('\33[1;35m[{:^20}]\33[m'.format(' Recuperação '))
elif md > 7.0:
    print('\33[1;32m[{:^20}]\33[m'.format(' Aprovado '))
print('-=-'*7)
print('Sua média foi de: \33[1;36m{:.1f}\33[m'.format(md))
print('-=-'*7)