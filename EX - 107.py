'''Crie um módulo chamado moeda.py que tenha as funções incoporadas
aumentar(), diminuir(), dobro(), metade().
Faça também um programa que importe esse módulo e use algumas
dessas funções'''
from ex107 import moeda
from cor import box_txt

box_txt('MODIFICADOR DE PREÇOS')

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')