n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O número {} é o maoir ! '.format(n1))
if n2 > n1 and n2 > n3:
    print('O número {} é o maior !'.format(n2))
if n3 > n2 and n3 > n1:
    print('O número {} é o maior !'.format(n3))
