from cor import box_txt

box_txt('ANT & DEP')

n = int(input('\33[1;32mDigite um número:\33[m  '))
print('O sucessor do número \33[32m{}\33[m é: \n\33[31m{}\33[m é o antecessor é: \33[31m{}\33[m'.format(n, n+1, n-1))
print('\33[1;32m-=-\33[m'*10)