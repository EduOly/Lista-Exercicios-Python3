from random import shuffle
print(' '*20)
print('{:=^40}'.format(' ORDEM DE APRESENTÇÂO '))
lista = ['Rafael', 'Lucas', 'Eduardo', 'Guanabara']
shuffle(lista)
print('A ordem de apresetação será assim:\n {}'.format(', '.join(lista)))
print('='*40)
