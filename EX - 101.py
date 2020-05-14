'''
Crie um programa que tenha uma função chamada voto() que vai receber 
como parâmentro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleição'''
#Com 18 a 64 voto obrigatorio
#Abaixo de 18 não vota 
#Acima de 65 voto opcional 

print('\33c')

def voto(y):
    from datetime import date #Importanto a função dentro da função economisa muinta mémoria
    year_day = date.today().year
    ida = year_day - y
    if ida >= 18 and ida <= 63:
        return f'Com a idade de {ida} anos \33[1;32m[VOTO OBRIGATORIO]\33[m'
    elif ida < 18:
        return f'Com a idade de {ida} anos \33[1;31m[VOTO NEGADO]\33[m'
    elif ida >= 64:
        return f'Com a idade de {ida} anos \33[1;33m[VOTO OPCIONAL]\33[m'

#Programa principal
nasc = int(input('Em que ano você nasceu?: '))
print(voto(nasc))