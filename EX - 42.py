print('{:=^38}'.format(' \33[1;32mTRIÂNGULO\33[m '))
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

if n1 < (n2+n3) and n2 < (n1+n3) and n3 < (n2+n1):
    print('\33[1;32m[Pode formar um triangulo]\33[m')
    if n1 == n2 == n3:
        print('\33[34m[È um Equiláteros!]\33[m')
    elif n1 != n2 != n3 != n1:
        print('\33[34m[È um Escaleno]\33[m')
    else:
        print('\33[34m[È um Isósceles]\33[m')
    print('=' * 27)
else:
    print('\33[1;31m[Não pode virar um triângulo]\33[m')

