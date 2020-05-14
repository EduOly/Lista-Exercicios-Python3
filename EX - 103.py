'''Faça um programa que tenha uma função chamada ficha(), que 
recebe dois parâmetros apcionais: o nome de um jogador e quantos 
gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jagador, mesmo
que alguns dados não tenha sido informado corretamente.'''

print('\33c')

def ficha(nome='<<desconhecido>>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#Programa princinpal
print('-'*30)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
