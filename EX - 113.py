'''Reescreva a função leiaint() que fizemos no desafio 104. Incluindo agora
a possibilidade de digitação de um número de tipo inválido. aproveite e crie
também a função leiaFloat() com a mesma funcionalidade'''

print('\33c')

def leiaInt2(x=0):
    """[Função que faz validação de valor se são interio ou não]

    Keyword Arguments:
        x {int} -- [valor a receber inteiro] (default: {0})

    Returns:
        [int] -- [retorno de valor somente interio]
    """
    while True:
        try:
            n = int(input(x))
        except Exception as erro:
            print('\33c')
            print(f"\33[1;31mERRO: por favor, digite um valor inteiro válido\33[m")
        except KeyboardInterrupt:
            print('\33c')
            print('\33[1;31mO usúario decidio não informar dos dados\33[m')
            n = 0
            return n
            
        else:
            return n

def leiaFloat(x=0):
    """[Finção que valida se o valor e real ou não e força para o usuário 
    somente digitar valores reais validos ]

    Keyword Arguments:
        x {float} -- [recebe valor real ] (default: {0})

    Returns
        [floar] -- [retorna somente valor real válido]
    """
    while True:
        try:
            num = float(input(x))
        except Exception as erro:
            print('\33c')
            print(f'\33[1;31mERRO: por favor, digite um número real válido\33[m')
        except KeyboardInterrupt:
            print('\33c')
            print('\33[1;31mO Usuário não quis informa os dados!\33[m')
            num = 0 
            return num
        else:
            return num

#Programa principal

num_int = leiaInt2("Digite um valor Inteiro: ")
num_float = leiaFloat("Digite um valor Real: ")

print(f'O valor inteiro digitado foi {num_int} e o real foi {num_float}')