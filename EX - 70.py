print('-'*40)
print('{:^40}'.format('LOJA SUPER BARATÃO '))
print('-'*40)
tot = mil = menor = 0
mpr =' '
c = 1 
while True:
    pro = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    cond = ' '
    tot += preco
    if c == 1:
        menor = preco
        mpr = pro
    if preco < menor:
        menor = preco
        mpr = pro
    if preco >= 1000:
        mil += 1
    c += 1 
    while cond not in 'SN':
        cond = str(input('Quer continuar? [S / N] ')).upper().strip()[0]
        if cond == 'S':
            print('-'*40)
            print('{:^40}'.format(' NOVO PRODUTO '))
            print('-'*40)
        if cond == 'N':
            break
print('{:-^50}'.format(' FIM DO PROGRAMA '))
print(f'O Total da compra foi R${tot :.2f}')
print(f'Temos {mil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {mpr} que custa R${menor :.2f}')
print('-'*50)