from cor import box_txt
box_txt('DESCONTO')
pr = float(input('Informe o valor do produto: '))
ds = pr-(pr*(5/100))
print('O valor do desconto será de R${:.2f}'.format(ds))