'''Aprimore o DESAFIO 093 para que ele fucione com vários jogadores, incluido um sistema de visualização de detralhes do aproveitamento de cada jogador.'''
def lin(msg):
    print('\33c')
    print('-'*30)
    print(f'{"|":<}{msg:^28}{"|":>}')
    print('-'*30)

lin('CADRASTRO DE JOGADORES')

jogador  = dict()
game = list()
gols = list()
sair = ''
ato = 0

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partidas {p}? ')))
        
      
    jogador['total'] = sum(gols)
    jogador['gols'] = (gols[:])
    gols.clear()
    game.append(jogador.copy())
    while True:
        sair = str(input('Quer continuar? [S/N] ')).upper()[0]
        if sair in 'SN':
            break
        print('\33[1;35mERRO!\33[m, Apenas Sim ou Não.')
            
    if sair == 'N':
        break
    else:
        print('-'*30)

print('-='*25)
print(f"{'Cod nome':<}{'gols':^28}{'total':>}")
print('--'*30)
for h in range(0, len(game)):
    print(f' {h} {game[h]["nome"]:<}{str(game[h]["gols"]):^28}{game[h]["total"]:>3}')
print('--'*30)

ato = 0
while True:
    ato = int(input('Mostrar dados de qual jogagor? (999 para parar)'))
    if ato > len(game) and ato < 998:
        print(f'ERRO! Não existe jogador com o código {ato}!')
        print('-'*30)
    elif ato == 999:
        break
    else:
        print(f"--- LEVANTAMENTO DO JOGADOR {game[ato]['nome']}:")
        for k, v in enumerate(game[ato]['gols']):
            print(f" => No jogo {k} fez {v} gols. ")
        print('-'*30)
print(f'{"<< VOLTE SEMPRE >>":^30}')





