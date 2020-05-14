'''Crie um pacote chamado utilidadesCev
que tenha dois módulos internos chamados
moeda e dado.
Transfira todos as funções utilizadas nos desafios 
107, 108 e 109 para o primeiro pacote e mantenha tudo fucionado'''

from ex111.utilidadescev import moeda
print('\33c')
p = float(input('Digite um valor: R$'))
moeda.resumo(p, 60, 45)