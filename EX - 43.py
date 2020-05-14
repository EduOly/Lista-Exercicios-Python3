print('\33[1;32m{:=^30}\33[m'.format(' IMC '))
#Entrada
alt = float(input('[Qual é a sua altura](m): '))
pes = float(input('[Qual é o seu peso](kg):  '))
#variaveis
md = alt*alt
imc = pes/md
#Condiçoes aninhadas
print('\33[32m=\33[m'*30)
if imc <= 18.5:
    print('\33[31m{:^30}\33[m'.format('Está abaixo do peso'))
elif imc > 18.5 and imc <= 25.0:
    print('\33[32m{:^30}\33[m'.format('Peso ideal!'))
elif imc > 25.0 and imc <= 30.0:
    print('\33[31m{:^30}\33[m'.format('Sobrepeso!'))
elif imc > 30.0 and imc < 40.0:
    print('\33[31m{:^30}\33[m'.format('Obesidade!'))
elif imc > 40.0:
    print('\33[31m{:^30}\33[m'.format('Obesidade mórbida!'))
print('\33[32m=\33[m'*30)