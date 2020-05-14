'''
Faça um progrma que leia 5 valores númericos
e guarde os em uma lista.
No final, mostre qual foi o maior e o menor
valor digitado e as suas respequitivas posiçoes 
na lista'''

print('\33c')
print('-'*50)
print(f"{'|':<0}\33[1;32m{' LISTA NÙMERICA ':^48}\33[m{'|':>0}")
print('-'*50)
num = []
for c in range(0, 5):
    num.append(int(input(f"Digite o {c}ª valor: ")))
posiM = []
Pme = []
maxi = max(num)
mini =  min(num)
for p , l in enumerate(num):
    if l == maxi:
        posiM.append(p)
    if l == mini:
        Pme.append(p)
print('-'*50)
print(f"{'|':<0}Os Numeros digitados foram {num}{'|':>1}")
print('-'*50)
print(f'O maior valor é {maxi} que está nas posíções: ', end='')
for v in posiM:
    print(f'{v}', end='..')
print(f'\nO menor valor é {mini} que está nas posições: ',end='')
for f in Pme:
    print(f'{f}', end='..')
print('\n')