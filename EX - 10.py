print('{:=^25}'.format(' CT VIRTUAL '))
print('{:=>20}'.format('== US1.00 == R$3.27 =='))
ct = float(input('Informe o valor que tu tem na carteira: '))
print('Com R${:.2f} reais posso comprar US{:.2f} dolares.'.format(ct, ct/3.27))
