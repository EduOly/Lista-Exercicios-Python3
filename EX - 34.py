print('=+'*15)
print('{:=^30}'.format(' EMPRESA '))
print('=+'*15)
sal = float(input('Qual o valor do seu Sálario?: R$'))
if sal > 1250:
    print('O Seu sálario terá um almento de \33[32m R${:.2f} Reais\33[m '.format(sal+(sal*(10/100))))
if sal <= 1250:
    print('O Seu sálario terá uma almento de \33[32m R${:.2f} Reais\33[m '.format(sal+(sal*(15/100))))
else:
    print()
print('\03[1;32;0m=+\33[;;m'*15)