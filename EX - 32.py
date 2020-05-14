from datetime import date
print('{:=^20}'.format(' BISEXTO '))
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISEXTO!'.format(ano))
else:
    print('O Ano de {} não é bisexto!'.format(ano))