'''
Faça um progrma que leia o sexo de uma pessoa, mas 
Só aceite os valores de 'M' e 'F'.Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''
sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Digite seu sexo:[M / F] ')).upper().strip()[0]
    if sex == 'F':
        print('Seu sexo é feminino ai que delicia !')

    elif sex == 'M':
        print('Blz meu veio!')