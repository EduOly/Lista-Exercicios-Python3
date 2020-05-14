num = 0
cont = 0
print(' '*10)
print('{:=^30}'.format(' LOGIN '))
while num != 999:
    num += 1
    cont += 1 
    num = int(input('\33[1;34mQua é a senha?: \33[m'))
print('='*30)
print('\33[1;32mNúmero de tentativa: \33[1;31m{}\33[m \33[1;32mvezes\33[m\33[m'.format(cont))
print('='*30)
print(' '*10)