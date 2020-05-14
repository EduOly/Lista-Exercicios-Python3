'''
Faça um progrma que leia nome e peso de 
de várias pessoas, quardando tudo em uma lista. No final, mostre:
A)Quantas pessoas foram cadrastradas.
B)Uma listagem com os pessoas mais pessadas.
C)Uma Listagem com as pessoas mais leves.
'''
print('\33c')
P = list()
data = list()
print('='*30)
print(f"{'[':<}{'SYS ACADEMIA':^28}{']':>}")
print('='*30)

while True:
    data.append(str(input('[ Nome ]: ')))
    data.append(float(input('[ Peso ]: ')))
    cons  = str(input('Deseja continuar [S / N]: ')).upper()[0]
    P.append(data[:])
    data.clear()
    if cons == 'N':
        break

print(' '*10)
print('='*30)
print(f"{'[':<}{'ALUNOS':^28}{']':>}")
print('='*30)
print(f"{'Nome'}{'':^22}{'PESO':>}")
print('='*30)

for c in range(0, len(P)):
    print(f"{P[c][0]:-<25} {P[c][1]:>.1f}")

print('='*30)
print(f"\33[1m{'Total de Alunos:':<28}{len(P):>}\33[m")
print('='*30)
print(' '*10)
print(f"{'[':<}{'MAIS PESADO A ABAIXO PESO':^28}{']':>}")

print('='*30)
print('MAX PESO')
print('-'*30)

for d in range(0, len(P)):
    if P[d][1] > 70:
        print(f"{P[d][0]} com peso de: {P[d][1]}kg.")

print('='*30)
print('PESO ABAIXO')
print('-'*30)

for f in range(0, len(P)):
    if P[f][1] < 50:
        print(f"{P[f][0]} com peso de: {P[d][1]}kg.")
