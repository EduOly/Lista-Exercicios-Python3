from math import hypot
from cor import box_txt

box_txt('HYPOTENUSA')
op = float(input('Valor do cateto oposto: '))
ad = float(input('Valor do cateto adjacent: '))
print('O valor da hypotenusa é de {:.2f} '.format(hypot(op, ad)))
print('='*40)