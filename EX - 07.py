print('\33[1;31m-=-\33[m'*10)
print('{:=^36}'.format(' \33[32mSIS MEDIA\33[m '))
print('\33[1;31m-=-\33[m'*10)
n1 = float(input('Informe a sua primeira nota: '))
n2 = float(input('Informe a sua segunda nota: '))
print('A sua média é de: \33[1;32m{}\33[m'.format((n1+n2)/2))
md = (n1+n2)/2
if md >= 5.0:
    print('\33[1;32mVocê passou parabéns!\33[m')
else:
    print('\33[1;31mEstude mais você está em recuperação!\33[m')
print('\33[1;31m-=-\33[m'*10)