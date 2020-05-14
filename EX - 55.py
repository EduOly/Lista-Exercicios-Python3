'''Faça um programa que leia o peso de cinco pessoas.
No final mostre qual foi o maior e o menor peso
lidos'''
maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input(f'qual pesso da {c} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {} e o menor pesso {}'.format(maior, menor))