somaidade = 0
md = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('-----{}ª PESSOA ----'.format(c))
    nome = str(input('informe seu nome: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

md = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(md))
print('O homen mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Ao total são {} mulheres com menos de 20 anos.'.format(totmulher20))
