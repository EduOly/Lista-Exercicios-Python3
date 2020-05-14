print('-=-'*13)
print('\33[32m{:=^39}\33[m'.format( ' MRV '))
#entrada de dados do usúario
vc = float(input('Qual o valor da casa?: R$'))
sl = float(input('Qual o valor do seu salário?: R$'))
pa = int(input('E quantos anos você vai pagar?: '))
#Variaveis
pr = pa*12
Vpr = vc/pr
controle = sl*(30/100)# saber 30% do valor do Salário o indíviduo

#Saída de dados
print('-=-'*13)
if Vpr < controle:
    print('\33[1;32mSeu finâciamento foi aprovado,\nsua parcela ficára R${:.2f} em {} vezes!\33[m'.format(Vpr, pr))
else:
    print('\33[1;31mSeu finânciamento não foi aprovado !\33[m\n'
          '\33[1;31mSua parcelá exeder 30% do seu salário!\33[m')
print('-=-'*13)