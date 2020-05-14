'''Adapte o código do desafio 107, criando uma
função adicional chamada moeda() que cosiga mostra
os valores como um valor monetário formatado'''

from cor import box_txt
from ex108 import moeda
box_txt('MODIFICADOR DE PREÇO FORMATADO')

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')