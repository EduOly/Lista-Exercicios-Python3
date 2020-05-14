from time import sleep
print('{:=^40}'.format(' \33[1;33;mSIS TYPE\33[m '))
print('\33[1;31m-=-\33[m'*10)
# Sim ou não de estrutura booleana
bin = ['\33[1;32mSim\33[m', '\33[1;31mNão\33[m']
#Entrada
al = input('Digite algo: ')
print('-=-'*10)
print('PROCESSANDO.....')
sleep(2)
#Variaveis

sp = al.isspace()
nu = al.isnumeric()
alf = al.isalnum()
ma = al.isupper()
mi = al.islower()
ti = al.istitle()
cp = al.capitalize()
#Saidá
print('Qual tipo?: \33[32m{}\33[m'.format(type(al)))

if sp == True:
    print('Tem, espaço?: {}'.format(bin[0]))
else:
    print('Tem, espaço?: {}'.format(bin[1]))

if nu == True:
    print('È númerico?: {}'.format(bin[0]))
else:
    print('È númerico?: {}'.format(bin[1]))

if alf == True:
    print('È alfanúmerico?: {}'.format(bin[0]))
else:
    print('È alfanúmerico?: {}'.format(bin[1]))

if ma == True:
    print('Está em maiúsculo?: {}'.format(bin[0]))
else:
    print('Está em maiúsculo?: {}'.format(bin[1]))

if mi == True:
    print('Está em minúsculo?: {}'.format(bin[0]))
else:
    print('Está em minúsculo?: {}'.format(bin[1]))

if cp == True:
    print('Está capitalizado?: {}'.format(bin[0]))
else:
    print('Está capitalizado?: {}'.format(bin[1]))

print('\33[1;31m-=-\33[m'*10)

