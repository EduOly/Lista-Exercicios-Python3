print('='*25)
n = int(input('Informe um número: '))
num = int(input('{:=^20}\n'
                '\33[1;36m[ 1 ] para binario\33[m\n'
                '\33[1;36m[ 2 ] para octal\33[m\n'
                '\33[1;36m[ 3 ] para hexadecimal\33[m\n'
                '[ Escolha as opçoes ]: '.format(' Menu ')))
print('='*23)
if num == 1:
    print(f'\33[1;32mSeu número em binário,\nficara assim: {n:b}\33[m'.format(n))
elif num == 2:
    print(f'\33[1;32mSeu número em octal,\nficarar assim: {n:o}\33[m'.format(n))
elif num == 3:
    print(f'\33[1;32mSeu número em hexadecimal,\nficarar assim: {n:X}\33[m'.format(n))
else:
    print('Opção invalida, tente novamente!')
print('='*23)