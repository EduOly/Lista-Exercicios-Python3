while True:
    n = int(input('Que ver a tabuada de qual valo?: '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')