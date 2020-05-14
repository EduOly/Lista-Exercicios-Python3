from random import choice
n1 = str(input('Primeio aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
print("O Aluno ecolhido é {}".format(choice(lista)))