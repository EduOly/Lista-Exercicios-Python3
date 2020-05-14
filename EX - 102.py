'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será um
valor lógico (opcional) indicando se será mostrado ou não na tela o processa de 
cálculo do fatorial.'''
print('\33c')

def fatorial(num, show=False):
    """[summary]

    Arguments:
        num {int} -- O número a ser calculado.

    Keyword Arguments:
        show {bool} -- (opcional) Mostra ou não a conta (default: {False})

    Returns:
        [int] -- O valor do Fatorial de um número num.
    """
    print('-='*20)
    from math import factorial
    fc = factorial(num)
    if show == False:
        return fc
    elif show == True:
        while num > 0:
            print(f'{num}', end='')
            if num > 1:
                print('x', end=' ')
            else:
                print(' = ', end='')
                return fc
            num -= 1

print(fatorial(5))
print()
        
