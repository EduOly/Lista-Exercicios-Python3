from random import randint
print('-='*15)
print('{:^30}'.format('VAMOS JOGAR PAR OU IMPAR'))
print('-='*15)
v = 0
while True:
    gamer =  int(input('Diga um valor: '))
    pc = randint(0, 10)
    soma = gamer + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo =  str(input('Par ou Impar? [P / I]: ')).strip().upper()[0]
    print(f'O computador digitou {pc} e o jogador {gamer}. Total {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else: 
            print('Você PERDEU!')
            break
    if tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER!. Você venceu {v} vezes')
