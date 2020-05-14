'''Modifique as funções que foram criadas no desafio 107 
para que elas aceitem um parâmetro a mais, informando se o valor 
retornado por elas vai ser ou não formatado pela função moeda(), 
desevolvida no desafio 108'''

from cor import box_txt
from ex109 import moeda
box_txt('MODIFICADOR DE PREÇO FORMATADO')

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')