'''
Crie um programa que crie uma matriz de
dimensão 3X3 e prencha com valores lidos 
pelo teclado.
No final mostre a matriz na tela, com a 
formação correta'''

print('\33c')
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l}, {c}]: '))
print('-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()
print('-'*30)
print(' '*10)