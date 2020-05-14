'''
Criar um programa que vai ler vários números
a colocar em uma lista.
Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares
digitados, respectivamente.
Ao Final, mostre o conteúdo das trẽs listas gerados.
'''
print('\33c')
lista = []
impa = []
pare = []
c = 0
while True:
    lista.append(int(input('Digite os valores: ')))
    cont = str(input('Deseja continual? [S / N]: ')).upper()[0]
    if lista[c] % 2 == 0:
        pare.append(lista[c])
    else:
        impa.append(lista[c])
    c += 1 
    if cont == 'N':
        break
print('-='*30)
print(f'A lista origina ficou {lista}')
print(f'A lita com valores pares : {pare}')
print(f'A A lista com valores imapares: {impa}')
