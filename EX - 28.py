from random import randint
from time import sleep
print('-=-'*20)
print('>>> Adivinhe número gerado pelo PC entre 0 & 5! >>>')
print('-=-'*20)
num = int(input('Informe o número: '))
print('PROCESSANDO...')
sleep(3)
cn = randint(0, 5)
if num == cn:
    print('Parabens o número gerado\n foi {}, você acertou!.'.format(cn))
else:
    print('Error tente novamente o numero foi {}.'.format(cn))
