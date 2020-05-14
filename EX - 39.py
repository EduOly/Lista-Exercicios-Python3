from datetime import date
nas = int(input('Informe sua data de nascimento: '))
ano = date.today().year
ida = ano - nas
if ida < 18:
    print('está muito novo, falta {} anos'.format(18-ida))
elif ida == 18:
    print('Essa é a hora de se alistá')
elif ida > 18:
    print('Passou do tempo, mais de {} anos'.format(ida - 18))