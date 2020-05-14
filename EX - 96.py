'''Faça um programa que tenha uma função chamada área(), que 
receba as dimensães de um terreno retangulor(largura e comprimento)e
mostre a área do terreno.'''

def lin(sms):
    print('\33c')
    print('-'*30)
    print(f'{"|":<}{sms:^28}{"|":>}')
    print('-'*30)


def area(larg, comp):
    ar = larg * comp
    print('-'*43)
    print(f'  A área de um terreno {larg:.0f} X {comp:.0f} é de {ar:.0f}m²')
    print('-'*43)
    

#Programa principal
lin('CALCULAR ÁREA DE UM TERRENO')
la = float(input('DIGITE A LARGURA: '))
co = float(input('DIGITE A COMPRIMENTO: '))
area(la, co)
