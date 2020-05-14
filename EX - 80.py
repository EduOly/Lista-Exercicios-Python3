'''
Crie um programa onde o usuário possa
digitar cinco valores numéricos e cadrastre-os em
uma lista, já na posição correta de inserção(sem o usar o sorted)
No final, mostre a lista ordenada na tela.
'''

print('\33c')
lista = list()
for c in range(0, 5):
    num = int(input(f'Digite o {c}ª valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)    
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)
