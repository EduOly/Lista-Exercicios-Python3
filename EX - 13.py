from cor import box_txt
box_txt('SALARIO')
sl = float(input('Informe o valor do seu salário:  R$'))
ds = sl+(sl*(15/100))
print('O Seu salário de R${:.2f} vai para R${:.2f} '.format(sl, ds))