num = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print('-'*40)
print(f'Você digitou os valores {num}')
print('-'*40)
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
    print('°'*40)
else:
    print('O número 9 não foi digitado !')
    print('°'*40)
if 3 in num:
    print(f'O valor 3 apreceu na {num.index(3)+1}ª posição')
    print('°'*40)
else:
    print('O número 3 não foi digitado !')
    print('°'*40)
print(f'Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
print('\n')
