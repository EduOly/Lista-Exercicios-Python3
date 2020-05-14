'''Crie uma tuplapreenchida com os 20
primeiro colocados da tabelas do campeonato Brasileiro
da Futebol, na ordem de colocação. Depois mostre:
A)Apenas os 5 primeiros colocados.
b)Os ultimos 4 colocados da tabela.
c)Uma lista com os times em ordem olfabetica.
d)Em que posção na tabela está o time da Chapecoense.
'''
print(' '*10)
print('\33[1;32m-\33[m'*80)
print('{:=^100}'.format(' \33[1;33mTABELA\33[m DO \33[1;32mBRASILEIRÃO\33[m '))
print('\33[1;33m-\33[m'*80)

tabela = ('Flamengo','Santos','Palmeiras','Grêmio','AthleticoPR',
'SãoPaulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia',
'Vasco','AtléticoMG','Fluminense','Botafogo','Ceará','Cruzeiro','Chapecoense','Avaí')

print('-='*40) 
print('\33[1;32mOs 5 primeiros colocados são:\33[m', end='')
print('(', end='')
for c in tabela[:5]:
    print(c, end=', ')
print(')')
print('-='*40)
print('\33[1;32mOs ultimos 4 colocados da tabela são: \33[m',end='')
print('(', end='')
for d in tabela[-4:]:
    print(d, end=', ')
print(')')
print('-='*40)
print('\33[1;32mA lista em ordem alfabetira é: \33[m', end='')
print('(', end='')
alfa = sorted(tabela)
for e in range(0, 18):
    print(alfa[e], end=', ')
    if e == 3:
        print('\n',end='')
    if e == 10:
        print('\n', end='')
print(')')
print('-='*40)
print('\33[1;33mA posição do time Chapecoense e a\33[m \33[1;32m{}ª.\33[m'.format(tabela.index('Chapecoense'+1)))
print('-='*40)
print(' '*10)

