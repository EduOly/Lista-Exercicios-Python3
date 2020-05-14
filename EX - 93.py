'''Crie um programa que gerencie o proveitamento de um jogador de futebol.O programa vai ler o nome do jogador e quantas partidas ele jogou.Depois vai ler a quantidade de gols feitos em cada partida.No final, tudo isso será quardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

print('\33c')

print('='*30)
print(f"{'|':<}{'APROVEITAMENTO':^28}{'|':>}")
print('='*30)
print(' ')

jogador = dict()
games = list()

 
jogador['nome'] = str(input('Nome do Jogador: '))
jogos = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, jogos):
    games.append(int(input(f"    Quantos gols ma partida {c}? ")))
   
jogador['gols'] = games[:]
jogador['total'] = sum(games)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f"O Campo {k} tem o valor {v}.")
print('-='*30)

print(f"O jogador {jogador['nome']} jogou {jogos} partidas.")
for p, v in enumerate(jogador['gols']):
    print(f"   => Na partida {p}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")
print(' ')