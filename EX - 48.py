print('\33[1;32m[{:=^31}]\33[m'.format(' MULT 3 '))
so = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0 :
        cont += 1
        so += c
print('\33[1;32m-=-\33[m'*11)
print('A Soma entre \33[1;31m0 a 500\33[m, de todos os {}\nnúmeros multiplos de 3 é: \33[1;32m[{}]\33[m'.format(cont, so))
print('\33[1;32m-=-\33[m'*11)
