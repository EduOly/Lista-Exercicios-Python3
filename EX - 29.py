from time import sleep
print('-=-'*10)
print('<{:-^27}>'.format(' PARDAL '))
print('-=-'*10)
vl = int(input('Informe a velocidade do veiculo: '))
print('PROCESSANDO......')
sleep(2)
if vl > 80:
    print('Você excedeu o  limite de velocidade,\nem {:.0f} km/h e deverar pagar R${:.1f} reais em multa !.'.format((vl-80.0), 7*(vl-80)))
if vl < 30:
    print('Fela da puta tá desfilando? multa de R$1.000 reais pra você.')
else:
    print('Parabéns continui respeitando nosso limite de velocidade!.')