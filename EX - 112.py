from ex112.utilidadecev import moeda
from ex112.utilidadecev import dados
print('\33c')
p = dados.leiaDinheiro('Digite um valor: R$')
moeda.resumo(p, 60, 45)