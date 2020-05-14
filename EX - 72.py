print('-'*40)
print('{:^40}'.format(' \33[1;34mPOR EXTENSSO\33[m '))
print('-'*40)
while True:
    valor = int(input('Digite o valor de 0 a 20: '))
    num = ('zero', 'um', 'dois', 'treze', 'quatro', 'cinco', 'seis','sete','oito','nove','dez','onze','doze','treze','quatoze','quize','dezeseis','dezesete','dezoito','dezenove','vinte')
    quan = len(num)
    if valor <= 0 or valor > quan:
        print('\33[1;31m[ERRO]\33[m \33[1;34m-Valor invalido!-\33[m ')
        print('-'*40)
    else:
        print('O valor digitado foi: \33[1;32m{}\33[m'.format(num[valor]))
        break
print('-'*40)