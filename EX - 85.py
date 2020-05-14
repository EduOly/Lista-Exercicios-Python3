'''
Crie um programa onde o usuário possa
digitar sete valores numéricos e cadrastra-os em 
uma lista única que mantenha separados os valores 
pares e ínpares.No final, mostre os valores pares e ímpares
em ordem crescente.
'''
print('\33c')
num = [ [] , []]
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('+='*25)
print(f'os valores pares foram {sorted(num[1])}')
print(f'Os números ímpares foram {sorted(num[0])}')
print('+='*25)
