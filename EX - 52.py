#-----DESAFIO 52-----
#FAça um progrma que leia um número
#inteiro e diga se ele é ou não um
#número primo.
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\33[32m',end='')
        tot += 1
    else:
        print('\33[31m',end='')
    print(f'{c}',end=' ')
print(f'\n\33[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print('É por isso ele è PRIMO')
else:
    print('Não é PRIMO')
