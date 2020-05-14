print('{:=^20}'.format(' TRIÂNGULO '))
n1 = float(input('\33[30;41mPrimeiro valor: \33[m'))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
if n1 < (n2+n3) and n2 < (n1+n3) and n3 < (n2+n1):
    print('Pode formar um triângulo!')
else:
    print('não pode virar um triângulo!')