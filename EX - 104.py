'''Crie um programa que tenha a função leiaInt(), que vai
funcionar de farma semelhante á função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
EX:
n = leiaInt('Digite um n')'''

print('\33c')

def leiaInt(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[1;31m[ERRO] Digite um número válido.\33[m')
        if ok:
            break
    return valor




#Programa principal
n = leiaInt('Digite um número: ')
print(f'\33[1;32mVocê acabou de digitar o número {n}\33[m')