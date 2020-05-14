print("{:=^30}".format(" BOM FIM VIAGENS "))
via = float(input('Quantos quilometros foi a viagem: '))
if via <= 200:
    print('O valor sa sua viagem foi de: R${:.2f} reias'.format(via*0.50))
else:
    print('O total do valor a pagar ser de R${:.2f} rais.'.format(via*0.45))
