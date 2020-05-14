print('{:=^30}'.format(' DESAFIO 38 '))
print('-=-'*10)
n1 = int(input('Informe o Primeiro número: '))
n2 = int(input('Informe o Segundo número: '))
print('-=-'*10)
if n1 > n2 :
    print('\33[1;32m---O primeiro valor é maior---\33[m')
elif n2 > n1:
    print('\33[1;32m---o segundo valor é o maior---\33[m')
else:
    print('\33[1;31m---Não exiter valor maior,\nos dois são iguais---\33[m')
print('-=-'*10)