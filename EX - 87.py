'''
Aprimore o desafio anterior,mostrando
no final:
A)A soma de todos os valores pares digitados.
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda linha'''

print('\33c')
print('='*20)
print(f"{'|':<0}{'ADD MATRIZ ':^18}{'|':>1}")
print('='*20)
print(' '*10)
matriz = [[0,0,0],[0,0,0],[0,0,0]]
p = 0
for l in range(0, 3):
    for c in range(0, 3):
     matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
     if matriz[l][c] % 2 == 0:
            p += matriz[l][c]
print(' '*10)
print('='*20)
print(f"{'|':<0}{' MATRIZ ':^18}{'|':>1}")
print('='*20)
print(' '*10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        
    print()
print(' '*10)
print('='*20)
print(f"{'|':>0}{'DADOS':^18}{'|':>1}")
print('='*20)
print(' '*10)
s = 0
for l in range(0, 3):
    s += matriz[l][2]
print(f'A soma de todos o valores da matriz e {p}')
print(f"A soma dos valores da terceira fileira é {s}")
print(f"O maior valor da seunda fileira é: {max(matriz[1])}")
print(' '*10)