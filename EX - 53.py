print('{:=^30}'.format(' POLINDROMO '))
fr =  str(input('Digiter a frase: ')).strip().upper()
pal = fr.split()
junt = ''.join(pal)
iv = fr[::-1]
if junt == iv:
    print('É um plinomio')
else:
    print('Não é')