print('\33[31m{:=^30}\33[m'.format(' GBARBOSA '))
#Entrada
pr = float(input('[Qual o valor do produtor?](R$): '))
cond =  int(input('\33[32m{:=^30}\33[m\n'
                  '[ 1 ] DINHEIRO / CHEQUE\n'
                  '[ 2 ] À VISTA NO CARTÂO\n'
                  '[ 3 ] ATÈ 2X NO CARTÂO\n'
                  '[ 4 ] 3X OU MAIS NO CARTÂO\n'
                  'SELEÇÂO: '.format(' MENU ')))
print('='*30)
#Sáida
if cond == 1 :
    print('\33[32mO valor do produtor com 10% de desconto,\nserár R${:.2f} reais \33[m'.format(pr-(pr*(10/100))))
elif cond == 2:
    print('\33[32mO valor do produto com 5%  de desconto,\nserár R${:.2f} reais \33[m'.format(pr-(pr*(5/100))))
elif cond == 3:
    print('\33[34mNão terá desconto!\33[m')
elif cond == 4:
    print('\33[31mO valor do produto terá um acresimo de 20%,\no valor ficarár de R${:.2f} reais \33[m'.format(pr+(pr*(20/100))))
print('='*30)