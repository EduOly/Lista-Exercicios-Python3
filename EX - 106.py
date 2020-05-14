'''Faça um mini-sistema que utilize o interactive Help do 
Python. O usuário vai digitar o comonado e o manual vai 
aparecer. Quando o usuário digitar a palavra 'Fim', o programa
se encerrará.
OBS:Use cores.'''


print('\33c')
from time import sleep
c = ('\33[m',   # 0 - sem cor
    '\33[0;30;41m', # 1 - vermelho
    '\33[0;30;42m', # 2 - verde
    '\33[0;30;43m', # 3 - amarelo
    '\33[0;30;44m', # 4 - azul
    '\33[0;30;45m', # 5 - roxo
    '\33[7;30m',    # 6 - branco
    )


def tit(msg, cor=0):
    tam = len(msg) + 4
    print(f"{c[cor]}", end='')
    print('~'* tam)
    print(f'  {msg}')
    print('~'*tam)
    print(f"{c[0]}", end='')
    sleep(1)

def ajuda(cmd):
    tit(f'Acessando o manual do comando \'{cmd}\'', 4)
    print(c[6], end='')
    help(cmd)
    print(c[0])
    sleep(2)


#Programa principal
comando = ''
while True:
    tit("SISTEMA DE AJUDA PYHELP", 3)
    comando = str(input('Função aou Biblioteca > '))
    if comando.upper() == 'FIM':
        tit("Até LOGO", 1)
        break
    else: 
        ajuda(comando)