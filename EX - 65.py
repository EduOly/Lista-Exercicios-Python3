'''
Cria um programa que leia várias números inteiros pelo
teclado. No final da execução, mostre a média entre todos os 
valores e qual foi o maior e o menor valores lidos. O programa
deve pergrama deve pergundo ao usuário se ele quer ou não continuar a digitar 
'''
cont = ''
soma = c = 0 
maior = menor = 0
while cont in 'Ss':
    n = int(input('Digite um número: '))
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += n  
    c += 1
    if c == 1:
        maior = menor = n 
    if  maior > menor:
        maior  = n
    else:
        menor = n
    
print('Você digitou {} números e a média foi {:.2f}'.format(c, (soma / c)))
print('O maior valor foi  {}  e o menor foi {}'.format(maior, menor))